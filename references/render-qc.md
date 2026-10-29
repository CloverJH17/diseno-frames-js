# Render, exportación y control de calidad

## Contenido

Evidencias; revisión de imagen; video; captura opcional; archivo final; límites. No aplica una misma batería a todo: revisa lo pertinente al medio y al cambio. Para perfiles de plataforma, accesibilidad y lectura de métricas, consulta [plataformas y calidad](plataformas-y-calidad.md); para escucha y eventos, [sonido por eventos](sonido-por-eventos.md).

## 1. Tres niveles de evidencia

Estructural: archivos, referencias, formatos y tiempos existen. Geométrico: contenido cabe, sus relaciones son correctas y no hay recortes involuntarios. Perceptivo: jerarquía, dibujo, ritmo, identidad y emoción funcionan. Una herramienta puede ayudar en varios niveles sin certificar los demás.

Entrega un informe proporcional: qué se comprobó automáticamente, qué se observó y qué sigue pendiente. No llames aprobado al material por superar un render. Diferencia archivo de revisión, entrega y aprobación editorial.

## 2. Imagen vectorial

Comprueba que el SVG se analiza, que sus referencias se resuelven y que `viewBox`, dimensiones e IDs son coherentes. Revisa grupos, rutas, texto y recursos raster incorporados. Validez de XML no demuestra que la forma sea correcta.

Observa tamaño final y miniatura para jerarquía, y amplía para curvas, uniones y detalles. Prueba alfa sobre fondos claros, oscuros y de color. Una cuadrícula dibujada detrás no demuestra transparencia; revisa el canal real o la geometría correspondiente.

Comprueba fuentes y significado de editable. Si el destino es un editor específico, úsalo cuando esté disponible para revisar máscaras, filtros y texto. Una captura PNG solo certifica esa representación visual, no toda la editabilidad del SVG.

Una imagen derivada de un cuadro debe tener composición completa y contenido legible. No heredes texto a mitad de animación. Verifica que la exportación no cambie dimensiones, recorte o color de forma inesperada.

## 3. Video antes del render completo

Muestra los estados de máxima legibilidad. Si la composición falla allí, corrígela antes de pulir movimiento. Captura también inicio, desarrollo y salida de acciones importantes. Densifica muestras en convergencias, máscaras y transiciones.

Una hoja de contacto revela variedad, densidad y continuidad. No certifica fluidez ni sonido. Doce o quince cuadros pueden ser útiles en una pieza; otra duración y complejidad necesitan un muestreo diferente. Revisa cuadros vecinos de las uniones cuando haya riesgo de salto.

La lectura se comprueba al tamaño de uso, con permanencia real y zonas de interfaz pertinentes. No existe una zona segura exacta universal. No reduzcas textos indefinidamente para conservar todo el contenido.

## 4. Disponibilidad y determinismo

Verifica la API temporal: segundos e índice no son intercambiables. Decide duración efectiva y cantidad de cuadros. Espera `document.fonts.ready`, comprueba familias necesarias y decodifica imágenes. Recursos fuera del DOM necesitan su propia señal de disponibilidad.

Prueba buscar A, luego B y volver a A. Diferencias pueden revelar estado acumulado, azar, fuentes, media o reloj sin controlar. Igualdad en esa muestra no prueba toda la película ni portabilidad entre equipos. Para simulaciones acumulativas define reconstrucción o caché determinista.

## 5. Helper conservado

`../scripts/capture_frames.py` toma muestras de un HTML local con `seek(t)` o `renderFrame(f)`, guarda PNG, hoja de contacto y un informe. Necesita Python, Pillow, Playwright y navegador disponible; no instala ninguno. Puede recibir navegador explícito y detecta rutas de Chrome/Edge en Windows.

Sus opciones de resolución y fps son parámetros, no estándares. Por defecto usa 1080×1920 y 30 fps: cámbialos según el proyecto. En modo fotogramas redondea el tiempo solicitado al índice correspondiente; revisa el argumento efectivo registrado.

La comparación A→B→A utiliza bytes PNG en el entorno de captura. No mide gusto, sincronía de voz, todos los solapamientos ni todas las máquinas. La hoja de contacto es ayuda de inspección, no un certificado.

El helper desactiva animaciones al capturar. Sirve a escenas reconstruidas por tiempo; una animación CSS autónoma puede verse alterada. Antes de adoptarlo, comprueba que no cambie el contenido que pretendes examinar. Tampoco comprueba por sí mismo todos los recursos WebGL o externos.

## 6. Geometría sin falsos certificados

En DOM mide elementos relevantes y considera sus transformaciones. Una caja de grupo grande puede ocultar colisiones entre hijos. En Canvas el DOM solo ve un lienzo; necesitas instrumentación del modelo para estudiar objetos internos.

Clasifica advertencias: recorte real, invasión de margen, colisión, superposición intencional o estado transitorio legítimo. Un objeto fuera de su caja local no está necesariamente fuera del área de uso. No ignores todos los avisos ni los conviertas todos en defectos.

## 7. Codificar y comprobar la salida

Separa imagen calculada y señal codificada. Intermedios sin pérdida preservan texto; JPEG añade otra compresión. H.264 y ciertos formatos de píxel suelen servir a entregas comunes, pero alfa, color y compatibilidad dependen del destino. No impongas un CRF o preset heredado.

Si hay segmentos, conserva parámetros compatibles y orden exacto; verifica las uniones y añade audio de forma coherente. Espera cierre y código de salida del codificador. Un proceso activo o un archivo parcial no constituye una exportación terminada.

Con ffprobe examina dimensiones, duración, frecuencia, cuadros cuando estén disponibles, códecs y audio. La frecuencia puede ser racional. Decodificar el archivo entero ayuda a detectar errores del flujo, pero no fallos artísticos.

Extrae muestras del archivo final, además del HTML. Revisa texto fino, bandas de gradiente, alfa si aplica y pérdida en partículas. Una resolución declarada mayor no demuestra detalle nativo.

## 8. Reproducción, escucha y accesibilidad

Reproduce a velocidad normal para ritmo y mezcla. Cámara lenta, por ejemplo 0,75×, ayuda a estudiar acciones, pero no sustituye velocidad normal. Si no puedes escuchar o revisar movimiento continuo, dilo sin certificarlo desde capturas.

Evita destellos y movimientos innecesariamente agresivos; estudia cambios de luminancia y orientación. Un video exportado no responde automáticamente a preferencias de movimiento reducido de una interfaz. No declares cumplimiento de accesibilidad por una única prueba visual.

Cuando un cambio y las verificaciones pertinentes pasan, entrega. Repite o amplía revisión si aparecen errores nuevos, no por acumular comprobaciones sin una incertidumbre concreta.
