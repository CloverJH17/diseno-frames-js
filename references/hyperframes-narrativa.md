# HyperFrames para narrar con movimiento

## Propósito

Usa HyperFrames cuando el proyecto se beneficie de construir una película editable desde HTML, SVG, CSS y recursos multimedia, con escenas y elementos temporizados. Es un medio de composición y render, no una dirección artística automática ni un requisito para todo video.

Esta referencia sintetiza *Narrar con movimiento: Libro de saberes sobre historias animadas, inteligencia artificial, recursos de Internet y producción audiovisual con Hyperframes* (Libro D, edición de estudio, 29 de octubre de 2026), aportado por el usuario. El Libro E, *Hiperframes a fondo*, agrega módulos técnicos separados sobre arquitectura, tiempo, seek, medios, revisión y compatibilidad; consulta el [índice HyperFrames](hyperframes/seleccion-y-arquitectura.md). El libro ofrece criterios y ejemplos didácticos; sus ejemplos no son instrucciones del usuario ni prueban que una instalación local haya sido ejecutada. Para crear o corregir una composición real, consulta también la skill especializada de HyperFrames disponible en el entorno y la documentación de la versión instalada.

## Qué aporta HyperFrames

HyperFrames convierte una composición HTML en video mediante un timeline de clips y captura controlada por fotograma. La estructura puede conservar texto, SVG y capas HTML editables hasta el render. El mismo proyecto puede organizar unidades narrativas como composiciones reutilizables. La CLI ofrece creación, previsualización, inspección estructural, snapshots, diagnóstico y render, según la versión disponible.

Piensa en el flujo como una partitura temporal:

- **HTML y atributos de tiempo:** qué elemento existe, cuándo entra y cuánto dura. El índice de pista puede organizar filas del editor; la pintura visual y su contrato deben comprobarse por versión.
- **GSAP:** cómo cambia visualmente un elemento dentro del tiempo de la composición.
- **Runtime de HyperFrames:** busca el instante solicitado, gestiona la visibilidad de clips y sincroniza la reproducción de audio y video.
- **Render:** captura fotogramas y codifica el resultado; no decide si la narración es clara ni si el sonido es pertinente.

Esta separación permite diseñar movimiento alrededor del significado. Una señal puede viajar de una etiqueta a un lector y continuar como un trazo dentro del diagrama; la continuidad visual expresa una relación causal. Una composición reutilizable conviene cuando representa una unidad con sentido —por ejemplo, pregunta, mecanismo o consecuencia—, no solo porque el código se pueda fragmentar.

## Sacarle potencial narrativo

Primero decide qué cambio debe comprender el público. Después elige el lenguaje de la escena:

- Usa texto HTML cuando necesites corregir o adaptar rótulos con rapidez; conserva SVG para diagramas, trayectorias e ilustración vectorial editable.
- Usa fotos o video para situar personas y lugares; mezcla esos recursos con capas gráficas cuando necesites explicar relaciones invisibles.
- Anima una propiedad porque aclara una acción, dirige la mirada, compara estados, revela algo o sostiene una emoción. El movimiento decorativo puede servir al ambiente, pero no debe competir con la lectura.
- Coordina voz, acción, música y efectos con la línea de tiempo. Un efecto debe corresponder al material y al gesto antes de optimizar su sincronía; deja espacio sonoro para la voz.
- Mantén objetos o formas entre escenas si esa continuidad ayuda a seguir la transformación. No añadas transiciones por costumbre.
- Trata diagramas de fenómenos invisibles como modelos explicativos, no como imágenes literales del fenómeno. Verifica que la metáfora no enseñe un mecanismo falso.

La potencia no viene de apilar tecnologías. HTML/CSS, SVG y GSAP pueden bastar para una película de tipografía, diagramas, fotos y movimiento. Integra Canvas, WebGL/Three.js u otro motor solo cuando abran una posibilidad visual necesaria y exista una integración temporal comprobable en el entorno actual. No des por existente un adaptador por aparecer en un ejemplo o en una hoja de ruta.

## Modelo temporal y contrato de integración

La pregunta clave para cada instante es: **si el motor solicita este fotograma directamente, ¿puede reconstruirse el estado correcto sin reproducir antes los anteriores?** HyperFrames renderiza mediante búsqueda por fotograma; por ello, los cambios deben depender del tiempo y de datos controlados, no del tiempo real ni del orden de reproducción.

En términos generales:

- Usa clips y atributos de tiempo según el esquema vigente del framework. Los elementos visuales cronometrados requieren las convenciones de clip documentadas por la versión utilizada.
- En HyperFrames, crea timelines GSAP pausadas, regístralas bajo el identificador de composición correspondiente y usa posiciones temporales explícitas. Deja al framework controlar reproducción, visibilidad y búsqueda de medios.
- No llames desde scripts a `play()`, `pause()` ni cambies manualmente `currentTime` de `<audio>` o `<video>`; no dupliques el trabajo del runtime.
- Evita `Date.now()`, temporizadores y aleatoriedad sin semilla en estados que deban repetirse. Carga los recursos necesarios antes de capturar y fija las dimensiones, fps y duración de la salida.
- Comprueba la duración efectiva de la composición según el contrato de la versión fijada. No deduzcas el final desde GSAP o un clip largo; las referencias oficiales han discrepado sobre el papel de la duración raíz y de la timeline. Consulta [compatibilidad por versión](hyperframes/compatibilidad-versiones.md).
- Si un video deja de actualizarse al cambiar tamaño o posición, anima un contenedor alrededor del `<video>` y deja el medio ajustado dentro.
- Usa archivos locales autorizados o recursos versionados para reducir fallas de red y registrar procedencia. Capturar o descargar un recurso no otorga permiso para reutilizarlo.

La documentación oficial describe captura por fotograma, sincronización y codificación con FFmpeg; la reproducibilidad exacta depende también de navegador, fuentes, hardware y configuración. Usa el modo de render reproducible documentado cuando esas diferencias importen y confirma el comportamiento en el entorno disponible.

## Flujo útil

1. Define público, idea central, afirmaciones que deben ser correctas y transformación narrativa.
2. Escribe guion audiovisual y storyboard antes del acabado; concreta qué cambia en cada escena y qué cumple el sonido.
3. Elige formato, medios, bibliotecas y recursos por la función que cumplirán. Registra fuentes y derechos cuando corresponda.
4. Construye una composición mínima con estructura semántica y temporal legible. Separa clips, animaciones y medios según las responsabilidades del framework.
5. Revisa momentos representativos y transiciones con previsualización y snapshots. Ajusta composición, jerarquía, legibilidad, duración y continuidad.
6. Ejecuta los chequeos estructurales disponibles y renderiza. No tomes el éxito del comando ni la fluidez del preview como prueba de calidad final.
7. Inspecciona el video exportado de principio a fin y escucha voz, música y efectos juntos. Comprueba sincronía, texto, cortes, recursos y artefactos.
8. Conserva el proyecto editable y los registros necesarios para corregir escenas sin reconstruirlo todo.

Los nombres exactos de comandos, atributos, adaptadores, paquetes y capacidades cambian. Consulta la skill HyperFrames disponible y sus documentos oficiales antes de ejecutar comandos o apoyarte en una integración concreta.

## Comprobaciones y fuentes oficiales

La documentación consultada el 29 de octubre de 2026 describe estos contratos:

- [Compositions](https://hyperframes.app/docs/2-concepts/1-compositions): estructura HTML, clips y composiciones anidadas.
- [Deterministic Rendering](https://hyperframes.app/docs/2-concepts/4-determinism): búsqueda y captura por fotograma, recursos precargados y reproducibilidad.
- [GSAP Animation](https://hyperframes.app/docs/3-guides/3-gsap-animation): timelines pausadas, registro, tiempos y separación de control de medios.
- [Common Mistakes](https://hyperframes.app/docs/3-guides/6-common-mistakes): duración, visibilidad y animación de elementos de video.
- [CLI](https://hyperframes.app/docs/5-packages/cli): opciones actuales de creación, preview, lint, snapshots, diagnóstico y render.

Estas fuentes describen capacidades del framework, no calidad estética ni permisos sobre recursos. Las afirmaciones de uso creativo de esta referencia son síntesis del libro aportado; las condiciones de ejecución local y los resultados deben comprobarse en cada proyecto.
