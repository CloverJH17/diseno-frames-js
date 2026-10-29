"""Capture a local deterministic HTML animation and optionally test A -> B -> A.

Dependencies: Pillow, Playwright, and an available Chrome/Chromium/Edge.
Does not install software or certify subjective motion/audio quality.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright


def times_arg(value):
    try:
        values = [float(x.strip()) for x in value.split(',')]
    except ValueError as exc:
        raise argparse.ArgumentTypeError('Use comma-separated seconds.') from exc
    if not values or any(not math.isfinite(x) or x < 0 for x in values):
        raise argparse.ArgumentTypeError('Times must be finite, nonnegative seconds.')
    return values


def positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError('Must be a positive integer.')
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--times', type=times_arg, required=True)
    parser.add_argument('--fps', type=positive, default=30)
    parser.add_argument('--width', type=positive, default=1080)
    parser.add_argument('--height', type=positive, default=1920)
    parser.add_argument('--api', choices=['auto', 'frame', 'seconds'], default='auto')
    parser.add_argument('--chrome', type=Path)
    parser.add_argument('--check-determinism', action='store_true')
    args = parser.parse_args()
    source = args.html.resolve(strict=True)
    if not source.is_file() or source.suffix.lower() not in {'.html', '.htm'}:
        parser.error('--html must identify a local HTML file.')
    if args.chrome and not args.chrome.is_file():
        parser.error('--chrome does not exist.')
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    report = {'source': str(source), 'fps': args.fps,
              'viewport': [args.width, args.height], 'samples': [],
              'browser_errors': [], 'determinism': None}
    failures = report['browser_errors']
    images = []
    try:
        with sync_playwright() as pw:
            candidates = [args.chrome,
                          Path(r'C:\Program Files\Google\Chrome\Application\chrome.exe'),
                          Path(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')]
            chrome = next((p for p in candidates if p and p.is_file()), None)
            options = {'headless': True, 'args': ['--allow-file-access-from-files']}
            if chrome:
                options['executable_path'] = str(chrome)
            browser = pw.chromium.launch(**options)
            page = browser.new_page(viewport={'width': args.width, 'height': args.height}, device_scale_factor=1)
            page.on('pageerror', lambda err: failures.append(str(err)))
            page.goto(source.as_uri(), wait_until='load')
            page.evaluate('async () => {await document.fonts.ready; await window.ready;}')
            api = args.api
            if api == 'auto':
                api = page.evaluate("typeof window.renderFrame==='function'?'frame':typeof window.seek==='function'?'seconds':'missing'")
            if api == 'missing':
                raise RuntimeError('No window.renderFrame(f) or window.seek(t).')
            function = 'renderFrame' if api == 'frame' else 'seek'
            report['api'] = function

            def capture(second):
                value = round(second * args.fps) if api == 'frame' else second
                page.evaluate('async a => {await window[a.fn](a.value); await document.fonts.ready; await Promise.all([...document.images].map(im=>im.decode()));}',
                              {'fn': function, 'value': value})
                missing = page.evaluate('[...document.images].filter(im=>!im.complete||im.naturalWidth===0).map(im=>im.src)')
                if missing or failures:
                    raise RuntimeError(f'Missing images: {missing}; browser errors: {failures}')
                return page.screenshot(type='png', animations='disabled'), value

            for index, second in enumerate(args.times):
                png, value = capture(second)
                filename = f'sample_{index:03d}.png'
                (output / filename).write_bytes(png)
                images.append(Image.open(io.BytesIO(png)).convert('RGB'))
                report['samples'].append({'requested_seconds': second, 'api_argument': value,
                                          'file': filename, 'sha256': hashlib.sha256(png).hexdigest()})
            if args.check_determinism:
                a, b = args.times[0], next((x for x in reversed(args.times) if x != args.times[0]), None)
                if b is None:
                    raise ValueError('Determinism check needs at least two distinct times.')
                first, _ = capture(a)
                capture(b)
                repeated, _ = capture(a)
                equal = first == repeated
                report['determinism'] = {'a': a, 'b': b, 'equal_png': equal,
                                         'first_sha256': hashlib.sha256(first).hexdigest(),
                                         'repeated_sha256': hashlib.sha256(repeated).hexdigest()}
                if not equal:
                    raise RuntimeError('A -> B -> A produced different PNG captures.')
            report['fonts'] = page.evaluate('[...document.fonts].map(f=>({family:f.family,status:f.status}))')
            browser.close()
        cellw = min(270, args.width)
        cellh = round(cellw * args.height / args.width)
        columns = min(4, len(images))
        sheet = Image.new('RGB', (columns * cellw, math.ceil(len(images) / columns) * (cellh + 28)), '#101820')
        draw = ImageDraw.Draw(sheet)
        for i, (im, sample) in enumerate(zip(images, report['samples'])):
            x, y = i % columns * cellw, i // columns * (cellh + 28)
            sheet.paste(im.resize((cellw, cellh), Image.Resampling.LANCZOS), (x, y))
            draw.text((x + 8, y + cellh + 6), f"{sample['requested_seconds']:g}s", fill='white')
        sheet.save(output / 'contact-sheet.jpg', quality=94)
        report['status'] = 'passed'
    except Exception as exc:
        report['status'] = 'failed'
        report['error'] = str(exc)
        raise
    finally:
        (output / 'capture-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'status': report['status'], 'samples': len(images), 'output': str(output), 'determinism': report['determinism']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
