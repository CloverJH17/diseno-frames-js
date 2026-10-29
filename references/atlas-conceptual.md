# Atlas conceptual: posibilidades, comparaciones y criterio

## Cómo leer los ejemplos

Son experimentos mentales para entender relaciones entre mensaje, forma y técnica. No son escenas aprobadas, plantillas, guiones reutilizables ni evidencia de proyectos realizados. No adoptes su estética o contenido por defecto. La producción necesita un concepto derivado del pedido actual.

## Recursos según lo que pueden comunicar

| Recurso | Posibilidad expresiva | Medio posible | Riesgo a revisar |
|---|---|---|---|
| Silueta simplificada | Reconocimiento y carácter | SVG/Canvas | Perder el rasgo esencial |
| Línea progresiva | Recorrido y construcción | SVG o Canvas | Trayectoria sin significado |
| Máscara | Revelación y cambio de contexto | SVG/CSS/Canvas | Ocultar demasiado tiempo |
| Capas con paralaje | Profundidad y recorrido | 2D/3D | Movimiento contradictorio |
| Texto por grupos | Articular una idea | DOM/SVG/Canvas | Fragmentar lectura |
| Partículas distribuidas | Ambiente, flujo o datos | Canvas/p5.js/GPU | Salvapantallas sin foco |
| Textura tenue | Materialidad y calidez | Raster, filtros o shader | Suciedad y compresión |
| Cámara que revela | Descubrir partes y escala | 2D/Three.js | Espectáculo sin información |
| Separación de piezas | Explicar estructura | SVG/Three.js | Distancias ambiguas |
| Transformación de forma | Relacionar conceptos | SVG o geometría calculada | Intermedios irreconocibles |
| Reflejo | Hacer visible una superficie | CSS/3D/shader | Apariencia engañosa |
| Gráfico proporcional | Comparar magnitudes | SVG/Canvas/DOM | Escala o unidades falsas |
| Corte | Cambiar idea con claridad | Composición audiovisual | Falta de ritmo o contexto |
| Audio reactivo | Relacionar sonido y forma | Análisis + dibujo | Relojes que divergen |

Pregunta si el recurso añade información, emoción pertinente o continuidad. Si no aporta ninguna, su costo probablemente supera su valor. Esto no exige eliminar toda ornamentación: una atmósfera también puede tener propósito.

## Caso A: una imagen sobre un instrumento

Supón una imagen educativa de un instrumento musical. Una primera solución acumula notas decorativas y un rótulo. Una mejor hipótesis puede enfatizar silueta, puntos de contacto y relaciones entre partes. SVG permite formas editables y conectores precisos; una textura externa puede aportar material si se acepta una entrega híbrida.

La comparación evalúa reconocimiento y comprensión, no cantidad de adornos. Si se convierten letras a curvas, la edición textual cambia. Si el instrumento representa un modelo real, no se inventan piezas ni proporciones significativas para hacerlo más bonito.

Este razonamiento se transfiere a otros objetos; no prescribe instrumentos como tema ni un estilo escolar.

## Caso B: explicar una interacción tecnológica

Una tarjeta se acerca a un lector y el sistema responde. Un diagrama SVG puede explicar el orden. Un modelo Three.js se justifica si orientación y posición de las partes importan. Etiquetas DOM/SVG mantienen lectura mientras el objeto cambia de ángulo.

Las ondas ilustradas son una metáfora si no simulan físicamente el campo. Una escena llamativa puede ser conceptualmente falsa. Se compara si la profundidad aclara más que una vista plana; no se escoge 3D solo porque el tema sea tecnológico.

## Caso C: comparar datos

Una imagen fija puede alinear barras y etiquetas; un video puede introducir las categorías en orden relevante. SVG conserva proporciones y edición; un sistema de componentes permite datos variables. La animación se justifica si guía hacia la diferencia importante.

No alteres valores para mejorar composición. Preserva escala, unidades, período y fuente. Una perspectiva dramática o superficies de volumen pueden hacer engañosa una comparación simple. El acabado profesional también consiste en resistir recursos que distorsionan evidencia.

## Caso D: mundo ilustrado por reglas

Un entorno imaginario puede construirse por familias de siluetas, luz y textura. Canvas o p5.js facilitan variación; SVG favorece edición de partes. Una cámara suave puede descubrir relaciones, siempre que los planos soporten el recorrido.

Compara una distribución uniforme de objetos con otra agrupada que deje foco. La segunda puede ser más expresiva con menos elementos. Si todo debe salir como vector puro, una textura raster o shader requerirá otra decisión y no se esconderá dentro de la entrega.

## Caso E: objeto como protagonista

Una cámara muestra un detalle que ayuda a comprender la función de un objeto. Three.js aporta perspectiva y oclusión; un shader específico podría aportar un material necesario. Si el mismo mensaje se explica con un dibujo limpio, ese camino merece comparación.

La iluminación debe ayudar a ver superficies, sin reflejos que inventen cualidades. Un giro bonito que impide leer la etiqueta puede empeorar la explicación. La pregunta es qué descubre la cámara, no cuánto se mueve.

## Caso F: sonido convertido en forma

Una pieza abstracta puede vincular amplitud a escala y frase musical a cambios de composición. No todas las bandas deben controlar todo. El análisis precalculado permite representar el mismo instante durante exportación.

Compara una reacción constante con una que reserve movimiento fuerte para acentos significativos. El silencio visual puede aumentar la fuerza del próximo evento. Si una partitura real aparece, respeta sus signos; si es metáfora, no la presentes como transcripción auténtica.

## Comparar sin convertir gusto en ley

| Variante | Qué observar | Qué no concluir automáticamente |
|---|---|---|
| Plana frente a profunda | Si el volumen aclara estructura | Que 3D siempre es mejor |
| Limpia frente a texturada | Foco, materialidad y lectura | Que textura equivale a calidad |
| Movimiento lineal frente a curvado | Peso y carácter | Que todo necesita easing complejo |
| Texto por bloque frente a caracteres | Comprensión y tiempo completo | Que más animación aumenta retención |
| Pocos detalles frente a muchos | Silueta y escala de uso | Que simplicidad siempre basta |

Formula la mejora como hipótesis y contrástala con la pieza. No inventes pruebas con público, resultados de retención ni aprobaciones. Véase [fundamentos](fundamentos-visuales.md) para diagnosticar y [revisión](render-qc.md) para comprobar.
