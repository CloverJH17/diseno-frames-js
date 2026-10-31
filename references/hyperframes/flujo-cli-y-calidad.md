# Flujo de inspección y calidad

## La CLI como instrumento de preguntas

La línea de comandos ayuda a conocer el proyecto, identificar defectos estructurales, observar instantes y producir la salida. No es un botón que certifique calidad. Los nombres, alias, opciones y disponibilidad cambian; consulta primero la ayuda de la versión instalada y sus skills.

Elige la comprobación según el cambio:

- Para entender el contenido y las composiciones, consulta el inventario o timeline que ofrezca la CLI actual.
- Para errores de estructura y contrato, usa los chequeos disponibles.
- Para composición y estados puntuales, captura muestras en tiempos relevantes.
- Para continuidad, usa preview y observa las transiciones.
- Para la entrega, renderiza y reproduce el archivo exportado de principio a fin.
- Para dimensiones, duración y códecs, consulta metadatos; esto no evalúa claridad ni emoción.

No asumas que un comando citado en este capítulo existe sin cambios. Alias antiguos y actuales pueden coexistir en documentos distintos.

## Evidencias que responden preguntas diferentes

| Evidencia | Puede mostrar | No demuestra por sí sola |
|---|---|---|
| Análisis estructural | Atributos, clips, IDs o errores detectables | Claridad narrativa o permisos |
| Snapshot | Un fotograma y sus relaciones visuales | Transición, sonido o película completa |
| Preview | Continuidad y ritmo percibido | Equivalencia perfecta con el archivo exportado |
| Render | Resultado codificado | Que se vio y escuchó correctamente |
| Metadatos de archivo | Duración, dimensiones y propiedades técnicas | Composición, exactitud o calidad perceptiva |
| Revisión humana completa | Legibilidad, ritmo, continuidad, causalidad y sonido | Licencias o hechos no contrastados |

El ciclo combina chequeo técnico con juicio editorial: intención y guion, composición, diagnóstico, muestras, preview, escucha, corrección, render y reproducción final. Ajusta su profundidad al alcance del cambio; no repitas todo el proceso para una modificación sin relación con las etapas ya aprobadas.

## Seleccionar muestras

Muestrea antes, durante y después de clips importantes; puntos densos de texto; límites de escenas; transiciones; cambios de escala; inicio y final; y acciones sincronizadas con sonido. Observa sobre todo estados de riesgo: solapamientos, carga de fuentes, entradas y salidas, material de video y Canvas/3D.

La comparación preview-render debe considerar versión, navegador, fuentes, recursos, tiempo solicitado y condiciones de captura. Una diferencia observada permite formular una hipótesis; identifica la causa con evidencia antes de corregir.

## Criterio de entrega

Reproduce el archivo final completo y escucha voz, música y efectos juntos. Confirma texto, cortes, recursos, artefactos, silencios, duración y sincronía. Conserva proyecto editable y procedencia necesaria para iterar. Reporta qué se revisó y qué limitaciones permanecen.

## Fuente y alcance

Síntesis del Libro E, capítulos 9 y 20–22, con apoyo de [CLI oficial](https://hyperframes.app/docs/5-packages/cli), [render determinista](https://hyperframes.app/docs/2-concepts/4-determinism) y [render y revisión](../render-qc.md). La investigación del libro no ejecutó HyperFrames ni un render.
