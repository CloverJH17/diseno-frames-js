# Composiciones y tiempo

## La composición contiene tiempo

HyperFrames representa una película mediante HTML y atributos temporales. La composición raíz, las escenas, los clips y los medios forman una estructura de montaje que el runtime consulta en instantes específicos. Los atributos declaran ventanas temporales; CSS y el orden del documento participan en la representación visual.

Piensa el tiempo con intervalos explícitos. Un clip que comienza en (s) y dura (d) ocupa conceptualmente ([s, s+d)): su instante final queda fuera de la ventana. Esta distinción ayuda a detectar estados que se animan hasta el límite, pero nunca llegan a verse.

## Decisiones que deben concordar

- La raíz identifica la composición, su lienzo y la duración según el contrato de la versión utilizada.
- Cada composición y clip conserva un identificador estable y un propósito revisable.
- Los elementos que deban aparecer y desaparecer con el timeline siguen la convención de clip documentada.
- Inicio, duración, pista y dimensiones se revisan como datos; el orden de pintura se confirma con la estructura/CSS de la versión real.
- Los medios locales, la carga de fuentes y los recursos asíncronos se preparan antes de solicitar el fotograma.
- Las escenas comparten continuidad cuando la historia lo necesita, aunque residan en archivos distintos.

No deduzcas duración, z-order ni semántica de pistas a partir de una propiedad aislada. La documentación pública y las skills oficiales han discrepado sobre esos contratos; consulta el registro en [compatibilidad por versión](compatibilidad-versiones.md).

## Continuidad y modularidad

Una escena debe poder describirse por lo que cambia y por lo que deja preparado para la siguiente. Una composición anidada resulta útil si encapsula una unidad con sentido o se reutiliza de forma coherente. Si un elemento cruza un corte, decide si se conserva, se transforma o se reemplaza; no hagas que el límite de archivo decida el montaje por accidente.

El contenido exacto puede separarse del movimiento para evitar que una cifra o etiqueta se duplique en varias escenas. La estructura de datos sirve para reducir errores y facilitar variantes, pero debe seguir siendo comprensible para quien edita el proyecto.

## Revisión temporal

Para cada clip importante, razona sobre tres estados: justo antes de entrar, durante la acción y al salir. Revisa también solapamientos, huecos, textos que quedan cortados en el límite y medios cuyo contenido no coincide con la ventana temporal.

Una captura aislada demuestra únicamente el aspecto de ese instante. No demuestra que la transición sea legible, que la duración narrativa sea adecuada ni que el archivo final conserve el montaje.

## Fuente y alcance

Síntesis del Libro E, capítulos 4–5, contrastada con [Compositions](https://hyperframes.app/docs/2-concepts/1-compositions), [Data Attributes](https://hyperframes.app/docs/2-concepts/2-data-attributes) y las [skills oficiales](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes). Los contratos concretos deben comprobarse contra la versión del proyecto.
