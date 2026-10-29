# Mapa de tecnologías y posibilidades

## Contenido

Responsabilidades; comparación; capacidades; límites; combinaciones. Es una comparación conceptual, no un benchmark ni certificación de integración entre versiones. Consulta [fuentes](fuentes-y-cobertura.md) para contratos concretos.

## Responsabilidades diferentes

Representar decide cómo existe la imagen. Animar organiza cambios. Componer coordina escenas y sonido. Renderizar calcula imágenes; codificar genera la entrega audiovisual. Verificar contrasta intención y resultado. Una herramienta puede participar en varias responsabilidades, pero no las vuelve equivalentes.

Una skill es conocimiento para el agente; una biblioteca es código reutilizable; un framework estructura trabajo; un formato representa información. Instalar uno no produce automáticamente una integración lista ni calidad artística.

| Recurso | Aporte | Posibilidad | Límite o costo |
|---|---|---|---|
| HTML/CSS/DOM | Elementos y disposición tipográfica | Editorial, tarjetas, títulos | Captura raster; web no resuelve ritmo audiovisual |
| SVG | Geometría declarativa | Ilustración, iconos, diagramas, mapas | Muchos nodos/filtros complican edición y render |
| Canvas 2D | Dibujo inmediato a píxeles | Paisajes, pinceladas, partículas | No conserva cada forma como vector editable |
| p5.js | Exploración creativa | Patrones y variación procedural | No garantiza composición ni exportación SVG |
| GSAP | Interpolaciones y timelines | Coreografía de propiedades | No dibuja ni monta por sí solo la película |
| Three.js | Escenas y gráficos 3D | Cámara, luz, volumen, materiales | Preparación espacial y recursos más complejos |
| WebGL/GLSL | Procesamiento gráfico GPU | Superficies y distorsiones | Depuración, compatibilidad; salida rasterizada |
| Lottie | Datos de animación reproducibles | Recursos portables compatibles | No representa cualquier efecto |
| HyperFrames | Composición audiovisual HTML | Escenas web y salida de video | Contrato temporal e integración específicos |
| Remotion | Componentes React por fotogramas | Escenas parametrizadas y datos | Todo debe respetar el reloj de render |
| FFmpeg/ffprobe | Procesar y analizar señales | Codificación, mezcla, diagnóstico | No corrige el diseño de los cuadros |

## HTML/CSS: escenografía editorial

Conviene para bloques de información, fotografías, alineaciones y texto. CSS convierte decisiones visuales en relaciones reutilizables. Máscaras y perspectiva de capas pueden producir profundidad aparente sin un modelo 3D.

El riesgo es trasladar una interfaz completa al video: demasiados paneles y estados sin idea central. La corrección es editorial. Antes de añadir glassmorphism o glow, verifica qué información debe leerse y qué material aporta al concepto.

## SVG: forma y edición

Conviene cuando contorno, relaciones entre partes o escalabilidad geométrica son esenciales. Grupos, rutas y máscaras sirven a imágenes y animación. Puede contener raster: el contenedor no garantiza que todo sea vectorial.

No suele ser la mejor representación para innumerables operaciones por píxel. Los filtros se evalúan sobre superficies y pueden variar entre destinos. Prueba el editor necesario; no deduzcas compatibilidad absoluta del navegador. Véase [SVG e imágenes](svg-imagenes.md).

## Canvas y p5.js: reglas que dibujan

Canvas facilita redibujar superficies y muchos trazos. p5.js facilita explorar geometría, ruido y patrones; dispone también de capacidades 3D según modo. No es exclusivamente 2D ni su `saveCanvas` exporta SVG nativo de forma general.

SVG conserva elementos; Canvas deja píxeles. Se puede compartir geometría y construir dos salidas, pero exige diseño explícito. No se recuperan automáticamente capas y semántica desde una captura.

## GSAP: la partitura

Relaciona entradas, énfasis, pausas y salidas. Stagger articula grupos; una timeline organiza acciones superpuestas. No decide qué contar ni crea geometría por animar propiedades.

En exportación, la timeline pausada necesita estados iniciales claros y actualización del dibujo. Callbacks que mutan estado externo pueden depender del recorrido. `seek` permite buscar posiciones; no certifica por sí solo determinismo de la composición completa.

## Three.js y shaders: volumen y superficie

Three.js organiza cámaras, materiales, luces y objetos. Sirve si perspectiva, oclusión o inspección de caras aporta comprensión. Mantén etiquetas legibles fuera de perspectivas que deformen información.

Shaders describen operaciones gráficas como ruido, ondulación o refracción estilizada. Pueden actuar en 2D. SDF y ray marching permiten otras formas de describir superficie y volumen, con costos de cálculo y depuración que deben justificarse.

Una cámara que descubre una parte aporta; una órbita constante durante una explicación puede quitar orientación. Una textura tenue puede unificar mejor que una distorsión a pantalla completa.

## Lottie: una animación que viaja

Interesa para iconos y acciones reutilizables en distintos entornos. La fidelidad depende del reproductor y propiedades compatibles. No convierte automáticamente una composición con shaders ni sustituye un motor de montaje.

Para video requiere carga completa y control del fotograma. Para editar dibujo fijo, el JSON animado no necesariamente reemplaza un original SVG con grupos.

## Frameworks y motor local

HyperFrames organiza composiciones HTML; Remotion trabaja con React y fotogramas. La elección depende del proyecto, no de una superioridad estética universal. Sus capacidades concretas se verifican en la versión elegida.

Un motor local HTML/JS puede bastar para una pieza, resolviendo carga, tiempo, captura y revisión por cuenta propia. Si el proyecto prohíbe un framework, estudiarlo no autoriza incorporarlo como dependencia.

## FFmpeg y la entrega

Procesa filtros, mezcla y codificación; ffprobe examina flujos y metadatos. La transparencia depende de toda la cadena. Mayor tasa de bits no arregla curvas torpes; reescalar no crea detalle original. Su función es preservar y transformar la señal diseñada.

## Combinaciones orientativas

| Necesidad | Núcleo | Complemento posible |
|---|---|---|
| SVG editable | Geometría SVG | JS para variantes; sin motor audiovisual |
| Texto y diagramas animados | DOM + SVG | Tiempo propio o GSAP y composición elegida |
| Mundo ilustrado | Canvas o SVG por planos | p5.js para explorar; raster si se acepta |
| Objeto espacial | Three.js | SVG/DOM para etiquetas y shader específico |
| Series de datos | Componentes y contenido separados | Framework si reduce trabajo real |
| Recurso multiplataforma | Lottie compatible | Motor con control de reproducción |
| Archivo ya compuesto | FFmpeg | Análisis y revisión perceptiva |

Antes de añadir una dependencia responde qué resuelve, qué alternativa simple existe, cómo sigue el reloj y qué pierde en edición o exportación. Si no hay respuesta concreta, mejora primero la propuesta visual.
