# Diseño sonoro por eventos: causalidad, identidad y mezcla

## Propósito

Este capítulo desarrolla cómo el sonido puede explicar acciones, construir un espacio, distinguir estados y dar ritmo a videos programáticos. Es una guía para comprender qué aporta una decisión sonora y qué evidencia permite evaluarla; **no es una lista de efectos que deban aparecer en cada pieza**.

Para la relación entre guion, voz y animática, consulta [guion y storyboard](guion-storyboard.md). La evaluación del audio dentro del archivo final se amplía en [render y revisión](render-qc.md). La consulta del libro fuente y sus límites está en [fuentes y trazabilidad](fuentes-y-cobertura.md).

## 1. Qué puede narrar el sonido

La banda sonora organiza atención, emoción, causalidad, materialidad, escala, distancia y continuidad. Puede anticipar una acción, hacer perceptible un contacto, sugerir peso, unir escenas o interrumpirse para que una frase tenga espacio. Su presencia no equivale por sí sola a dirección sonora: una pieza puede tener música, voz y decenas de pistas y seguir sin jerarquía.

Es útil separar cuatro problemas que suelen confundirse:

| Diagnóstico | Qué ocurre | Por qué no basta con subir volumen |
|---|---|---|
| Nivel | El evento adecuado está bajo en la mezcla | Más ganancia puede causar clipping y no cambia el timbre. |
| Sincronía | El ataque llega antes o después de la acción percibida | El archivo puede comenzar en el tiempo correcto y su transitorio audible llegar tarde. |
| Semántica | El sonido sugiere una acción distinta | Una explosión para un botón o una caja arrastrada para una ruta digital cambia la lectura. |
| Contraste | Cada sonido tiene la misma energía o huella | La audiencia no distingue acciones comunes de un hito narrativo. |

El silencio también puede tener función: pausa para comprender, anticipo de un impacto, ausencia expresiva o contraste con un clímax. A la vez, puede faltar por accidente un evento que explique una transformación. Es el contexto el que permite distinguir ambas cosas.

## 2. Diegético, editorial e híbrido

Un sonido **diegético** parece pertenecer al mundo representado: teclas, pasos, puerta, papel o máquina. Un sonido **no diegético** guía la interpretación desde fuera de ese mundo: música, golpe de montaje, riser o firma sonora. La animación permite combinar ambos o inventar una convención estilizada, siempre que conserve coherencia suficiente para ser leída.

La elección no depende de si el referente se ve realista. Un botón dibujado puede recibir un click exagerado de interfaz; una abstracción puede usar textura de metal o respiración para comunicar densidad. Lo importante es que el gesto acústico acompañe la intención y no se haga pasar por grabación oficial del producto o sistema operativo.

## 3. Familias sonoras como vocabulario, no como receta

| Familia | Asociaciones frecuentes | Preguntas de criterio |
|---|---|---|
| Click / tap | selección, activación, contacto breve | ¿Hay presión o respuesta visible? ¿Suena adecuado al peso del objeto? |
| Pop / tick | aparición ligera, unidad pequeña, señal de interfaz | ¿La escena pide ligereza o el sonido se volvió un tic repetido? |
| Teclado | escritura, trabajo, entrada de datos | ¿La acción realmente muestra tecleo? ¿Se necesita cada tecla o basta una textura agrupada? |
| Foley | roce, manipulación, tela, papel, pasos, objeto apoyado | ¿La materialidad da comprensión o impone realismo donde no hay objeto físico? |
| Impacto | llegada, colisión, énfasis o corte | ¿La masa aparente y la consecuencia justifican su energía? |
| Whoosh / desplazamiento | transferencia espacial, paso o velocidad | ¿El movimiento recorre espacio y hacia dónde? ¿Se repite el mismo barrido en funciones distintas? |
| Riser / tono progresivo | anticipación, acumulación o preparación | ¿Qué resolución prepara y cuándo llega? |
| Chime / confirmación | estado completo, logro, conexión | ¿El estado sí se completó? ¿Se diferencia del sonido que inicia la acción? |
| Glitch / error | fallo, anomalía, ruptura | ¿El tono humorístico/técnico es pertinente o se volvió un cliché? |
| Ambiente | ubicación, mundo, continuidad | ¿Sostiene la escena sin hacerse protagonista permanente? |
| Música | pulso, emoción, estructura y continuidad | ¿Refuerza el sentido o rellena cada hueco? |

Un catálogo puede describir un efecto por material, clase de evento, peso, carácter del ataque, zona espectral, duración de cola, estado de ánimo, perspectiva acústica y política de repetición. Estas propiedades ayudan a buscar alternativas y crear familias; el nombre del archivo, por sí solo, no basta para elegirlo.

## 4. Ataque, cuerpo y cola

Un efecto breve suele percibirse mediante tres zonas: **ataque**, primer gesto audible que permite localizarlo; **cuerpo**, región que define su material y energía; **cola**, resonancia, aire o decaimiento que lo integra en el espacio. El mismo evento puede sentirse seco y cercano con un ataque corto y cola mínima, o amplio y lejano con más desarrollo.

La selección también depende de espectro y dinámica. Si la voz enfatiza consonantes, un efecto agudo puede competir justo con la inteligibilidad. Un subgrave puede desaparecer en un altavoz móvil pequeño. Una mezcla muy comprimida puede hacer que todos los sonidos parezcan igual de importantes. El archivo original, la conversión y la plataforma también modifican la percepción.

La ganancia y el pitch no siempre ocultan la identidad de una muestra repetida. Cambiar ligeramente tono o duración puede seguir dejando reconocible el mismo whoosh. Para construir variación genuina, cambia fuente, envolvente, materialidad, ritmo o decide no sonorizar ese gesto secundario.

## 5. Sincronía perceptiva por eventos

La marca temporal del archivo no siempre coincide con el instante en que el oído reconoce su acción. Conviene distinguir:

- `file_start`: comienza el recurso en el timeline.
- `audible_onset`: primera señal que se puede oír.
- `attack_peak`: transitorio más perceptible del ataque.
- `visual_contact`: instante de presión, choque, encaje o cambio visual relevante.
- `decay_end`: final útil de la cola.

Un whoosh puede iniciar antes del movimiento como anticipación y culminar en la llegada. Un golpe puede llevar el ataque exactamente al contacto. Una cola puede seguir después del gesto como sensación de espacio. Un archivo que empieza al llegar un objeto puede sonar tardío si su ataque se acumula cientos de milisegundos más tarde.

A 30 fps, un cuadro equivale matemáticamente a 33,3 ms. Esa conversión sirve para localizar una muestra, pero **no establece una tolerancia perceptiva universal**. Los eventos suaves, anticipados o estilizados se juzgan distinto de un clic seco o un contacto preciso. Una medición de correlación entre pistas puede demostrar que comparten reloj; no certifica que el efecto suene natural.

La pregunta es relacional: ¿qué causa o idea sonora debe coincidir con qué estado visual? La respuesta puede ser anticipación, contacto, seguimiento, puente o pausa musical.

## 6. Cobertura con jerarquía

“Sonido para cada elemento” tiene sentido cuando se refiere a los **acontecimientos que llevan significado**. No significa un efecto por píxel, palabra, partícula o movimiento de cursor. Agrupar acciones como un evento compuesto evita saturación y conserva un contraste claro entre gesto principal y ambiente.

Una auditoría de escena puede recorrer acciones como estas:

| Acción visible | Decisión sonora que se puede explorar | Riesgo que examinar |
|---|---|---|
| Cursor presiona un botón | Click breve o microrespuesta | Si el cursor solo apunta, repetir clicks inventa interacción. |
| Hoja pasa | Roce de papel o pliegue | El sonido de página puede ser metáfora editorial, no material literal. |
| Objeto se desplaza y reposa | Fricción más apoyo | El foley puede sugerir peso o material no representados. |
| Texto aparece como un bloque | Un acento para el bloque | Sonorizar cada palabra compite con la narración. |
| Ruta se dibuja | Textura de escritura o movimiento progresivo | Un whoosh genérico puede borrar la diferencia entre trazar y volar. |
| Nodos se conectan | Tick, unión o una resolución breve | Cada nodo decorativo no necesita un pitido individual. |
| Propuesta recibe revisión | Aviso ligero, pausa de lectura | No adelantar la integración antes de que el estado cambie. |
| Cambio queda integrado | Gesto de unión y confirmación propia | Debe diferenciarse del click que inició el proceso. |
| Cámara revela otro espacio | Puente, corte musical o ambiente | La transición no tiene que sonar como un objeto físico. |

El movimiento de cursor, una retícula persistente o partículas de ambiente pueden compartir una cama sonora o permanecer en silencio. Un evento protagonizado puede usar un recurso único. Una capa ambiente también necesita rango dinámico y espacio para otras ideas.

## 7. Arquitectura de mezcla y prioridad

Se puede pensar en seis familias de pistas: voz, música, Foley/acciones, microinteracciones de interfaz, transiciones/impactos y ambientes. Son categorías de escucha, no una obligación de tener seis buses técnicos.

La voz hablada suele necesitar inteligibilidad, pero no siempre es protagonista. En un clip ASMR el Foley puede dirigir la experiencia; en una obra musical la pista puede ser la figura principal. La mezcla ordena planos según la intención concreta. El *ducking* es una posible relación entre voz y fondo, no la orden de bajar toda música continuamente. Ataques puntuales pueden ocupar un hueco o enmascarar una palabra incluso si la música general está baja.

LUFS integrados describen una dimensión de sonoridad media; rango dinámico, pico verdadero y saturación describen otras. El filtro `loudnorm` de FFmpeg implementa normalización basada en EBU R128, pero un objetivo configurable no significa que una plataforma lo exija. [Documentación FFmpeg `loudnorm`](https://ffmpeg.org/ffmpeg-filters.html#loudnorm).

El libro de origen utiliza **aprox. −16 LUFS integrados y −1 a −2 dBTP** como punto interno de partida para ensayar contenido hablado. No son niveles mágicos ni metas universales de TikTok, Reels, Shorts o Facebook. El ejemplo documentado en [el caso GitHub](caso-github.md) midió −16,37 LUFS y −1,78 dBTP para la versión con voz; esos números describen ese render, no su calidad perceptiva ni una norma de entrega.

La música, SFX y voz deben escucharse en el archivo codificado, no solo en stems WAV. Comprueba estéreo y mono cuando sea viable, además de un altavoz pequeño y auriculares. El paneo puede sugerir trayectoria, pero el contenido esencial no debería depender de un estéreo extremo.

## 8. Biblioteca, tendencias y derechos

Las categorías de búsqueda de un catálogo —foley, ambiente, transición, pop, teclado, glitch, impacto— ayudan a encontrar vocabulario. No prueban que el recurso esté bien grabado, sea apropiado o esté autorizado para tu caso. Examina ataque, cuerpo, cola, ruido, artefactos de corte, compresión, compatibilidad con móvil y relación con la escena.

Las licencias se comprueban por recurso y tipo de uso. “Royalty-free” no significa automáticamente dominio público, atribución opcional, uso en toda plataforma o permiso para compartir el archivo de audio sin integrar. Música incluida en el catálogo de una red puede estar limitada a su producto, región, cuenta o campaña. Guarda URL, autor, nombre de licencia, fecha de consulta, atribución requerida, permisos comerciales y plataformas permitidas.

Las tendencias son vocabulario cultural cambiante. Conviene diferenciar recursos estructurales (por ejemplo, syncopation o pausas), estilos cíclicos (glitch, speed ramp o beat sync), memes reconocibles y sonidos ligados a un catálogo o tendencia de una fecha. La presencia en una plantilla de edición no demuestra licencia de reutilización, autorización comercial ni efecto causal en retención. Las afirmaciones de popularidad requieren consulta fechada y evidencia de destino.

## 9. Modelo conceptual de evento

El recurso de audio describe lo que el efecto **es**. La colocación en la escena explica **por qué aparece ahí**. Un registro conceptual puede separar:

| Descripción del recurso | Decisión de timeline |
|---|---|
| `asset_id`, fuente, autor y URL | `scene_id` y `visual_event_id` |
| licencia, permiso comercial, atribución y fecha de revisión | `sound_asset_id` y licencia aplicable a este uso |
| material, peso, familia y recurrencia | `visual_anchor_ms` y `audible_onset_ms` |
| carácter de ataque, zona espectral y cola | motivo narrativo, ganancia, ducking y capas que compiten |
| notas de calidad y revisión auditiva | repetición justificada, alternativa de silencio y estado de aprobación |

Este modelo revela incertidumbres importantes: un campo `peak_reference` puede ser una marca editorial y no una medición de pico acústico; un sample puede existir sin licencia comprobada; un onset calculado automáticamente no indica si el oído reconoce el evento. Los metadatos no deben confundir una intención con un hecho medido.

## 10. Cómo evaluar un efecto y una escena

Estas preguntas pueden orientar una discusión editorial:

1. ¿El sonido corresponde a la acción, idea o material representados?
2. ¿Su peso, duración, ataque y espectro se sienten proporcionales?
3. ¿El ataque coincide con contacto, anticipación o seguimiento deliberado?
4. ¿La voz o el foco visual conservan prioridad cuando se requiere?
5. ¿La repetición aporta identidad o revela reciclaje del mismo sample?
6. ¿Existe contraste con el silencio y con otros eventos?
7. ¿La mezcla funciona al volumen de escucha previsto, en mono y en móvil?
8. ¿La pieza sigue comunicando la transformación esencial sin audio?
9. ¿La procedencia y los permisos están documentados para cada archivo?

Las métricas pueden medir nivel, recorte, silencio, offsets o cobertura declarada. El oído humano juzga además naturalidad, irritación, humor, claridad y fatiga. Si no fue posible reproducir y escuchar, se informa una revisión técnica incompleta en lugar de llamar al sonido “profesional” o “bien balanceado”.

## 11. Qué aporta TikTok y qué no

El aprendizaje sobre sonido de TikTok reúne tres niveles: lenguaje de montaje observado en catálogos, prácticas que describen herramientas y orientación publicitaria publicada por la plataforma. Las guías de TikTok for Business pueden recomendar sonido, narración, captions y propuestas tempranas para campañas; su objetivo comercial no demuestra una regla de edición orgánica ni una promesa de viralidad.

Beat sync, cortes al acento, *velocity edits*, mini-vlogs, glitches y sonidos de meme son posibilidades que pueden ayudar a una pieza cuando expresan su tono. No es obligatorio usar todos. Cortar al pulso en cada compás puede volver mecánico un contenido explicativo; una pausa antes del remate puede aportar más que un efecto viral. La métrica de retención no permite adjudicar causalidad a un sonido si no se controla qué más cambió.

Para campañas o publicación comercial, verifica las condiciones actuales de la biblioteca musical y del sonido en el destino correspondiente. No descargues ni traslades sin licencia un audio popular solo porque aparece en una plantilla o página de tendencias.

## Fuentes de consulta

- [TikTok for Business: Creative Codes](https://ads.tiktok.com/business/en-US/creative-codes) — distinción de funciones de música, voz y efectos en anuncios.
- [TikTok Commercial Music Library y uso comercial](https://ads.tiktok.com/resources/help/article/how-to-use-the-commercial-music-library?lang=es-419) — producto y disponibilidad de música comercial.
- [YouTube Audio Library](https://support.google.com/youtube/answer/3376882?hl=en) — catálogo y garantías limitadas al servicio.
- [Freesound: licencias](https://freesound.org/help/faq/) — CC0, CC BY y otras condiciones a revisar por recurso.
- [Mixkit: licencia SFX](https://mixkit.co/license/modal/sfxFree/) — términos particulares del catálogo.
- [Creative Commons CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) y [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — alcance y obligaciones de cada licencia.
- [W3C/WAI: captions pregrabadas](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html) — captions incluyen voz y sonidos no verbales significativos.

Son referencias vivas, no una certificación legal. Comprueba las condiciones vigentes antes de publicar y registra lo consultado.
