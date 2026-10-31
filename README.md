# Diseño Frames Js

**Un libro de consulta en crecimiento sobre imágenes SVG y videos con código.**

Diseño Frames Js reúne conocimiento, ejemplos analizados y fuentes para comprender cómo diseñar imágenes y piezas audiovisuales con herramientas de programación. Ayuda a comparar técnicas, entender qué aporta cada biblioteca y desarrollar criterio visual.

El objetivo es que el código sirva para crear composiciones más cuidadas, claras y expresivas. La calidad no depende de usar muchos efectos o tecnologías: depende de que la forma, el movimiento y los recursos respondan a lo que la pieza necesita comunicar.

## ¿Qué encontrarás aquí?

- Fundamentos de composición, jerarquía, tipografía, forma, color, luz y materialidad.
- Orientación para crear imágenes SVG editables e ilustraciones dibujadas mediante código.
- Comparaciones de HTML/CSS, SVG, Canvas, p5.js, GSAP, Three.js, shaders, Lottie, HyperFrames, Remotion y FFmpeg.
- Ideas para combinar dibujo, animación, composición, sonido y revisión.
- Ejemplos conceptuales que ayudan a razonar; no plantillas que deban copiarse.
- Un flujo de guion, bocetos y animática, con historia, personajes y ganchos pensados para redes.
- Una especialidad de motion graphics: acciones que explican, transformaciones, continuidad y un laboratorio mínimo de causa y respuesta.
- Criterios para zonas seguras de video e imagen, sonido por acciones, narración y revisión con subagentes cuando estén autorizados.

## Un ejemplo conceptual

El [caso GitHub](references/caso-github.md) muestra cómo un conflicto cotidiano puede transformarse en una breve explicación con acciones, voz, diseño sonoro y pruebas. El storyboard está hecho para estudiar la continuidad; es una reconstrucción del prototipo, no una plantilla para copiar.


### HyperFrames a fondo

El Libro E amplía la parte dedicada a HyperFrames como sistema para dirigir piezas audiovisuales. Sus capítulos están organizados como conocimiento de consulta, no como proyectos prefabricados:

- [Selección y arquitectura narrativa](references/hyperframes/seleccion-y-arquitectura.md): responsabilidades, elección de medios y modularidad con sentido.
- [Composiciones y tiempo](references/hyperframes/composiciones-y-tiempo.md): escenas, clips, ventanas y continuidad.
- [GSAP, búsqueda temporal y dibujo procedural](references/hyperframes/gsap-y-seek.md): estados reconstruibles, Canvas, 3D y propiedad de medios.
- [Catálogo, medios y procedencia](references/hyperframes/catalogo-y-medios.md): reutilización crítica, licencias y sonido causal.
- [Flujo de inspección y calidad](references/hyperframes/flujo-cli-y-calidad.md): evidencia estructural, visual, sonora y de archivo.
- [Compatibilidad por versión](references/hyperframes/compatibilidad-versiones.md): discrepancias documentales fechadas y límites de las conclusiones.

La guía puede servir tanto para una ilustración o un gráfico estático como para una composición audiovisual. También explica la diferencia entre un SVG con geometría editable y una imagen rasterizada, que se forma con píxeles.

## Cómo empezar

Abre [SKILL.md](SKILL.md) para conocer el enfoque y encontrar el capítulo pertinente. Las guías están en `references/` y se pueden leer por separado:

- [Guion y storyboard](references/guion-storyboard.md): empezar por lo que se cuenta y bocetar cómo ocurre.
- [Motion graphics](references/motion-graphics.md): transformar una idea en acciones, elegir técnicas por función y revisar qué se comprende.
- [Continuidad entre escenas](references/continuidad-escenas.md): conservar consecuencias, orientar la cámara y reconstruir estados al buscar el tiempo.
- [Antipatrones de motion](references/antipatrones-motion.md): diagnosticar una presentación involuntaria y corregir la capa responsable.
- [Redes y zonas seguras](references/redes-zonas-seguras.md): captar atención y proteger contenido de interfaces y recortes.
- [Colaboración y revisión](references/colaboracion-revision.md): coordinar subagentes y revisar con evidencia.
- [Fundamentos visuales](references/fundamentos-visuales.md): diagnosticar y mejorar una composición.
- [Dirección audiovisual](references/direccion-audiovisual.md): narrativa, gancho, ritmo, movimiento, mundo y sistema gráfico.
- [Plataformas y calidad](references/plataformas-y-calidad.md): perfiles, overlays, accesibilidad, exportación, pruebas y métricas con sus límites.
- [Mapa de tecnologías](references/mapa-tecnologias.md): entender y comparar herramientas.
- [Imágenes SVG](references/svg-imagenes.md): trabajar con geometría vectorial y editabilidad.
- [Ilustración procedural](references/ilustracion-procedural.md): construir dibujos a partir de reglas y código.
- [Técnicas visuales](references/tecnicas-visuales.md): explorar tiempo, movimiento y transiciones.
- [Sonido y sincronía](references/sonido-sincronia.md): integrar música, voz, efectos y texto temporizado.
- [Diseño sonoro por eventos](references/sonido-por-eventos.md): causalidad, Foley, sincronía, mezcla, bibliotecas, licencias y audio de videos cortos.
- [Voz y narración](references/voz-narracion.md): escoger voz, probar pronunciación, medir tomas y diferenciar captions y rótulos.
- [Arquitecturas](references/integracion.md): relacionar componentes y motores.
- [Render y revisión](references/render-qc.md): comprobar el resultado y entender qué demuestra cada prueba.
- [Atlas conceptual](references/atlas-conceptual.md): comparar recursos expresivos con situaciones imaginadas.
- [Mapa de skills](references/mapa-skills.md): conocer guías especializadas que pueden complementar el trabajo.
- [Fuentes y trazabilidad](references/fuentes-y-cobertura.md): consultar el origen de las ideas y las fuentes.
- [Bibliografía audiovisual](references/bibliografia-audiovisual.md): índice anotado de las 45 fuentes del libro de dirección audiovisual.
- [Caso de estudio: explicar GitHub](references/caso-github.md): aprender de las revisiones de un prototipo.

El aprendizaje combina libros de referencia, una bitácora crítica, propuestas y documentación técnica. Sus ejemplos ayudan a razonar sobre diseño; sus políticas particulares, cifras contextuales y tendencias no se convierten automáticamente en instrucciones para proyectos futuros. La tabla de [fuentes y trazabilidad](references/fuentes-y-cobertura.md) explica la cobertura y las ediciones.

No es necesario leer todo para cada tarea. Usa el índice para localizar lo que necesitas. Si estás creando, empieza por la intención visual y consulta las herramientas según la forma de imagen y el tipo de movimiento que requieras.

## Una distinción importante

Esta skill estudia cómo crear gráficos con código. Canvas y WebGL dibujan imágenes rasterizadas; SVG describe formas vectoriales editables. Una captura de Canvas, incluso guardada dentro de un archivo SVG, no se convierte por eso en geometría vectorial.

La skill también compara bibliotecas y otros recursos de consulta. Esa comparación sirve para comprender posibilidades, ventajas y límites; no significa que cada biblioteca venga instalada, que todas deban combinarse ni que cada integración haya sido probada.

## De dónde surge

La guía reúne aprendizajes sobre dirección audiovisual, motion graphics, bibliotecas, criterio visual y HyperFrames, además de documentación técnica y repositorios públicos enlazados en [Fuentes y trazabilidad](references/fuentes-y-cobertura.md).

## Estructura

```text
SKILL.md                  Entrada e índice de consulta
agents/openai.yaml        Nombre y descripción para la interfaz de Codex
references/               Capítulos y fuentes de consulta
assets/motion-causal/     Laboratorio opcional de SVG y tiempo controlado
```

La skill puede utilizarse con Codex cuando está disponible en su catálogo de skills. Sus capítulos también pueden leerse como una guía independiente.
