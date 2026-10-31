# Continuidad de acciones, objetos y cámara

## Cuándo consultar

Cuando una explicación salta entre tarjetas, se pierden consecuencias, la cámara desorienta o una exportación difiere al retroceder. Complementa [motion graphics](motion-graphics.md), [técnicas visuales](tecnicas-visuales.md) e [integración](integracion.md). Continuidad narrativa y estado computacional son cosas relacionadas: conservar identidad en la historia no obliga a reutilizar el mismo nodo DOM ni a filmar un solo plano.

## 1. Identidad y consecuencia

Decide qué sigue siendo lo mismo: un archivo, una forma, un personaje, una cantidad, una relación o una pregunta. Si el archivo se guardó, el corte no debe borrarlo sin explicación. Si la transformación cambia la identidad deliberadamente, diseña qué permite reconocerla.

Un mapa pequeño puede registrar por objeto su identidad, estado inicial, disparadores, estados resultantes, ubicación relativa, pertenencia y condiciones de salida. Solo añade esos datos cuando eviten un error o faciliten correcciones. Un mundo completo puede existir en el modelo aunque el encuadre muestre una parte.

La persistencia es **semántica**. Se pueden reconstruir escenas o usar subcomposiciones siempre que sus estados correspondan a lo ocurrido. Un único SVG persistente puede fallar narrativamente si todo se reinicia, mientras dos escenas independientes pueden conservar perfectamente la consecuencia.

## 2. Conectar dos momentos

Dibuja el último estado relevante de A junto al primero de B. Señala qué relación debe seguir el público:

| Relación | Posible enlace | Riesgo a observar |
|---|---|---|
| Misma acción | Continuar el gesto tras un corte | Reiniciar o duplicar el contacto |
| Misma identidad | Seguir el objeto, conservar un rasgo o hacer match cut | Confundirlo con otro objeto equivalente |
| Causa y resultado | Estímulo en A, respuesta en B | No dejar percibir el estímulo o anticipar la respuesta sin intención |
| Detalle y conjunto | Acercarse y regresar con anclajes | Que el detalle parezca otro mundo sin relación |
| Contraste | Corte directo con referencia común | Cambiar unidades o posiciones de modo que invalide la comparación |
| Cambio de contexto | Máscara, paso por una abertura o corte explícito | Presentar una transformación gráfica como relación factual falsa |

No inventes continuidad donde el contenido necesita separación. Un corte puede delimitar etapas o contrastar opciones. Una pausa también enlaza cuando permite asimilar el resultado anterior.

## 3. Mundo y cámara tienen funciones diferentes

El mundo contiene geometría, estados y relaciones; la cámara selecciona qué se conoce. Una cámara puede acercarse para revelar una articulación, seguir una transferencia o alejarse para mostrar el efecto en el conjunto. Pregunta qué información aporta y qué referencias permiten conservar orientación.

En 2D, un grupo transformado puede actuar como mundo y otra capa sostener rótulos. En 3D, separa trayectoria de cámara y objetivo. Comprueba pivotes, oclusiones, escala y legibilidad en estados intermedios. El paralaje sugiere profundidad; no convierte una composición de planos en una reconstrucción volumétrica.

Evita usar la cámara para encubrir objetos sin comportamiento. Si una tapa solo se acerca sin abrirse, quizá el mecanismo siga sin estar representado. No impongas movimiento: un encuadre fijo puede mostrar claramente estímulo, contacto y respuesta.

## 4. Consecuencia persistente con tiempo absoluto

Expresa `estado = F(t, contenido, estilo, semilla)` y dibuja todos los valores necesarios. «Persistente» no significa ejecutar una instrucción una vez y confiar en la reproducción previa. Al pedir directamente un instante posterior, el estado ya debe incluir consecuencias anteriores; al retroceder, debe reconstruir su estado anterior.

Una puerta puede derivar su apertura de una ventana temporal y la posición del objeto de otra. El orden causal se diseña en esas ventanas: señal llega → puerta se abre → objeto cruza. No dependas de un callback que cambie `abierto = true` solo cuando la reproducción atraviesa un punto.

DOM, SVG, Canvas, shaders y medios necesitan el mismo tiempo de composición y sus propios mecanismos de actualización. Para la implementación, lee [integración](integracion.md) y el módulo del motor elegido. En GSAP, [seek](https://gsap.com/docs/v3/GSAP/Timeline/seek()/) permite situar el reloj; los callbacks omitidos por defecto son una razón adicional para no basar el estado visual en efectos acumulativos.

## 5. Verificar las dos continuidades

**Narrativa:** observa llegada, contacto, respuesta y resultado. Sigue identidad, cantidad, contenido, orientación y significado de colores. Una igualdad de píxeles no demuestra que el público entienda la relación.

**Temporal:** pide A → B → A y otros saltos que atraviesen contactos y cambios de escena. Compara valores relevantes y capturas en un entorno fijado. Revisa también un instante anterior al primer evento y otro posterior al resultado: los extremos detectan estados que quedaron sin restaurar.

**En el archivo final:** observa cuadros vecinos de uniones y reproduce el recorrido a velocidad normal. El HTML y la codificación pueden introducir problemas diferentes. Anota qué se comprobó y qué sigue sin observarse; consulta [render y revisión](render-qc.md).
