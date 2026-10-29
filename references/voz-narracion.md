# Voz, narración y captions

## Propósito

La voz puede acercar una idea, aportar presencia humana, aclarar relaciones o establecer un tono. También puede ralentizar el montaje, competir con la acción o repetir texto que ya se entiende. Este capítulo ayuda a valorar qué gana una pieza con narración, cómo probar voz humana o sintética, cómo presupuestar su tiempo y cómo distinguir diálogo, captions y rótulos.

El punto de partida editorial se desarrolla en [guion y storyboard](guion-storyboard.md). Para música y foley consulta [sonido por eventos](sonido-por-eventos.md); para posición y perfil de pantalla, [redes y zonas seguras](redes-zonas-seguras.md).

## 1. Qué aporta cada canal

| Canal | Aporte frecuente | Riesgo de redundancia |
|---|---|---|
| Narración | contexto, explicación de relaciones, matiz y tono | La voz describe literalmente lo que ya dice cada rótulo y muestra la animación. |
| Texto visible | nombre propio, cifra, palabra clave, lectura en silencio y recuerdo | Se convierte en párrafo largo o segundo guion en pantalla. |
| Imagen/acción | proceso, causalidad, transformación, escala y relación espacial | Elementos decorativos repiten la narración sin aclarar qué ocurre. |

Una composición complementaria puede narrar “explora alternativas” mientras una línea se bifurca y la palabra clave queda visible un momento. No hace falta que todos los canales transmitan la misma oración al mismo tiempo. Tampoco es obligatorio que toda pieza tenga voz: una acción visual o un diseño sonoro pueden llevar la experiencia sin narrador.

## 2. Elegir una voz por adecuación, no por disponibilidad

Voz humana, TTS comercial, sintetizador local o lectura sin narración son alternativas. La decisión depende de la audiencia, el tono, el idioma, la dicción, los permisos, el costo, la privacidad, la reproducibilidad y la capacidad de corregir palabras puntuales.

Una prueba breve debe incluir material representativo: una pregunta con emoción, una frase explicativa, vocabulario técnico, nombres propios y el tipo de cierre esperado. Evalúa:

- naturalidad de frase y respiración;
- prosodia, énfasis y pausas;
- acento e idioma apropiados al público;
- pronunciación de marcas, siglas y anglicismos;
- nitidez de consonantes y facilidad de comprensión;
- consistencia entre tomas y segmentos;
- permiso de uso, atribución, costo y límites de clonación;
- disponibilidad real del modelo o proveedor y privacidad de los datos enviados.

Una voz instalada no implica que sus derechos cubran la publicación. El uso de un TTS tampoco autoriza imitar a una persona real ni elimina restricciones sobre el modelo. Guarda la versión del motor, nombre de voz y licencia junto con la toma si la reproducción futura importa.

## 3. Guion que cabe de manera expresiva

La duración hablada depende de la dicción, el idioma, el énfasis, las pausas y la dificultad del vocabulario; el conteo de palabras solo da una aproximación. Es más fiable crear una lectura de prueba, medir las tomas y comprobarlas en contexto con la imagen y música provisional.

Si una frase no cabe, puede ser mejor editarla, repartirla entre escenas, dejar que una acción comunique una parte o extender el tiempo. Acelerar una voz hasta que parezca apurada reduce claridad y tono. Si la animación ya existe, la voz puede adaptarse a esa temporalidad, pero conviene registrar que el guion llegó después. En una producción nueva, la prueba de voz puede servir para darle tiempo a la animática antes del acabado.

Las versiones segmentadas facilitan cambiar timbre o regrabar una oración sin repetir todo el video. Conserva texto exacto, tiempos editoriales y duración medida de cada toma. Deja ventanas de respiración para pausas y transiciones; los timecodes de frases no acreditan sincronía por palabra.

## 4. Pronunciación técnica en español

Las marcas, siglas y términos extranjeros pueden pronunciarse de varias maneras en comunidades distintas. Antes de grabar, decide cómo se dirán palabras clave como `Git`, `GitHub`, `commit`, `branch`, `merge` o `pull request`. La pronunciación de una voz de síntesis puede necesitar una grafía fonética o una pausa artificial para lograr inteligibilidad. Mantén la ortografía oficial en pantalla cuando corresponda y no traslades esa ayuda fonética a los rótulos.

Una transcripción editada también puede servir para distinguir pronunciación de escritura y prevenir desajustes en captions. Pide o verifica la lectura de nombres cuando el contexto lo requiera; no supongas que cada audiencia usa el mismo acento o anglicismo.

## 5. Mezcla y lugar de la voz

La voz no se hace clara por poner su ganancia “al cien”. Su inteligibilidad depende de nivel, ruido, dinámica, ecualización, timbre, ataques de música y efectos, y transitorios que coinciden con las consonantes. La música puede reducirse durante palabras mediante ducking, pero no tiene por qué desaparecer en toda frase. Un Foley prominente también puede enmascarar una sílaba aunque su volumen medio parezca bajo.

Conserva stems separados durante la revisión cuando sea posible. Comprueba la mezcla codificada y una salida previa, en altavoz pequeño y auriculares; prueba mono si el evento o paneo dependen del estéreo. Métricas de sonoridad y pico ayudan a detectar ciertos límites, pero no prueban naturalidad ni equilibrio subjetivo. Consulta [sonido por eventos](sonido-por-eventos.md) para estas distinciones.

## 6. Subtítulos, captions y rótulos

- **Subtítulo de diálogo:** reproduce la voz hablada.
- **Caption:** ofrece una alternativa textual sincronizada al audio; cuando un efecto, música o ruido tiene significado, puede necesitar describirse junto con el diálogo.
- **Rótulo gráfico:** añade un nombre, idea, dato o llamado. Puede resumir, no transcribir.

Las captions de video pregrabado son distintas de las etiquetas editoriales: la explicación de W3C/WAI para WCAG SC 1.2.2 indica que cubren diálogo, identidad de quien habla y sonido no verbal importante. [W3C/WAI: Captions (Prerecorded)](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html).

La sincronía puede ser por oración, línea o palabra según la intención y la capacidad real de alineación. Si solo se dispone de marcas por frase, no se declara alineación palabra por palabra. Se corrigen ortografía, puntuación, términos técnicos y segmentación gramatical. El texto permanece el tiempo suficiente para leerlo sin tapar la acción principal y queda en el perfil de pantalla adecuado.

## 7. Comprensión con y sin sonido

El modo silencioso es habitual y también es una prueba de comprensión: ¿se conserva el problema, el cambio y el resultado esencial? No es necesario transcribir toda la narración; sí ofrecer las señales visuales que permiten seguir la causalidad. De manera complementaria, captions accesibles describen la información sonora que no se encuentra ya presentada en otra forma disponible.

Un cierre puede repetirse en voz y texto cuando esa redundancia intencional ayuda a recordar. El criterio no prohíbe duplicar información: pregunta si cada repetición aumenta comprensión, reconocimiento o acceso, o si solo añade una segunda tarea de lectura.

## 8. Lo aprendido en la prueba de 30 segundos

La prueba explicativa de GitHub se produjo en español con una voz Kokoro disponible localmente. Se generó por segmentos y se midieron las duraciones reales. El guion mantiene GitHub en los rótulos, pero usa una ayuda de pronunciación distinta al generar voz; estas son decisiones específicas del ejemplo, no la voz predeterminada de la skill.

Las seis tomas duraron aproximadamente: gancho 3,33 s; repositorio 3,18 s; historial 3,76 s; ramas 3,08 s; revisión 3,77 s; cierre 2,68 s. Las ventanas editoriales incluyen entrada y separación entre frases, por lo que la duración de la locución y el intervalo de escena no son la misma magnitud. Los subtítulos se sincronizaron por oración, no a nivel fonético o de palabra.

El texto se editó para que la voz explicara sin llenar las escenas. La pista mantuvo voz, música y efectos separados y redujo la cama durante el diálogo. Se generó también una versión sin voz para comparar la pieza. El informe describe los archivos e indicadores, pero en esa revisión no se pudo escuchar el audio; por tanto, naturalidad, pronunciación y aprobación final requieren una escucha humana. El [caso de estudio](caso-github.md) y la documentación de cobertura registran el alcance completo.

## 9. Preguntas de cierre

- ¿La voz agrega una relación, tono o contexto que la imagen no da por sí sola?
- ¿Se puede escuchar cada palabra sin acelerar en exceso?
- ¿Pronuncia nombres técnicos con claridad para el público elegido?
- ¿Los captions corresponden al audio realmente exportado?
- ¿Los rótulos anclan conceptos sin transcribir el párrafo entero?
- ¿La historia central sigue comprensible sin sonido?
- ¿Se registraron origen, permiso y limitaciones de la voz?
- ¿La muestra final se revisó auditivamente en la velocidad y dispositivo previstos?

Estas preguntas abren la conversación creativa; no sustituyen el diseño concreto de la escena.
