# Selección y arquitectura narrativa

## Pregunta de partida

HyperFrames conviene cuando la pieza necesita una composición audiovisual editable en HTML, elementos temporizados y una salida de video controlada por el framework. El motor resuelve estructura y tiempo; no reemplaza dirección, guion, investigación, diseño de sonido ni criterio visual.

La selección no consiste en activar todas sus funciones. Consiste en encontrar una cadena donde cada recurso técnico permita una acción narrativa o mejore la revisión. Si SVG, HTML y CSS resuelven con claridad la pieza, sumar Canvas, 3D o un catálogo no la mejora automáticamente.

## Capas de responsabilidad

Conviene razonar por separado sobre:

- **Intención editorial:** qué debe comprender o sentir la audiencia, qué afirmaciones son verificables y qué cambia entre inicio y cierre.
- **Contenido:** datos, nombres, cifras, citas y fuentes que deben conservar exactitud.
- **Representación:** HTML para texto y estructura; SVG para geometría editable; Canvas o WebGL para dibujo rasterizado/procedural; medios reales para evidencia de objetos, lugares y acciones.
- **Coreografía:** cuándo aparece, cambia, se transforma o desaparece cada elemento.
- **Composición y reloj:** escenas, clips, duraciones, sincronía, dimensiones y control de reproducción.
- **Evidencia:** revisión estructural, observación visual, escucha y examen del archivo exportado.

Mantener estas capas diferenciadas facilita cambiar una representación sin reescribir el argumento y corregir tiempos sin duplicar hechos en varias escenas.

## Elegir la forma de una escena

Una escena separada tiene valor cuando representa una unidad que se puede revisar o comprender por sí misma: una pregunta, un mecanismo, una comparación o una consecuencia. Dividir el archivo solo por longitud de código puede fragmentar continuidad y aumentar los puntos de integración.

Las escenas pueden compartir una forma, objeto o trayectoria entre cortes. La arquitectura debe apoyar la progresión semántica: los límites de archivos no son necesariamente límites narrativos.

## Combinaciones y costo

| Necesidad perceptiva | Representación posible | Cuidado |
|---|---|---|
| Texto exacto y editable | HTML/CSS | Fuentes cargadas, contraste, recortes |
| Diagrama con geometría modificable | SVG | Legibilidad y escala |
| Muchos trazos, partículas o dibujo calculado | Canvas | Repintar desde el tiempo solicitado |
| Volumen o relación espacial difícil de aplanar | Three.js/WebGL | Integración temporal comprobable y carga |
| Apariencia real de un objeto o sitio | Foto/video autorizado | Procedencia, derechos y pertinencia |
| Patrón reutilizable con función clara | Catálogo HyperFrames | Adaptación visual y revisión del código instalado |

Una integración híbrida debe explicitar qué aporta cada capa. Una foto puede sostener la evidencia, mientras el SVG señala una parte y el texto explica una relación. Las simulaciones y metáforas deben distinguirse de mediciones reales.

## Criterio de aprendizaje

El ejemplo del lector RFID del libro *Hiperframes a fondo* ilustra causalidad y continuidad. Es un caso didáctico, no un tema o storyboard que se herede. La próxima pieza debe comenzar por su propia pregunta y su propio material.

Consulta [composiciones y tiempo](composiciones-y-tiempo.md) al definir estructura; [GSAP y seek](gsap-y-seek.md) para animación reproducible; y [catálogo y medios](catalogo-y-medios.md) para reutilización, procedencia y derechos.

## Fuente y alcance

Síntesis del Libro E aportado por el usuario, partes I, III y V; contrastada con la [introducción oficial](https://hyperframes.app/docs/1-startup/1-introduction) y la [guía de composiciones](https://hyperframes.app/docs/2-concepts/1-compositions). Los criterios son conocimiento de consulta, no un proyecto ejecutado ni una orden de usar HyperFrames.
