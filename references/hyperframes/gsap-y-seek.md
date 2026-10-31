# GSAP, búsqueda temporal y dibujo procedural

## Un fotograma debe ser reconstruible

En una composición que puede solicitarse en cualquier instante, el estado visual debe depender del tiempo pedido y de datos controlados. El mismo instante debe producir el mismo estado aunque el motor haya visitado antes un fotograma posterior.

Evita lógica acumulativa como `x += velocidad`, temporizadores de reloj real o azar no sembrado para estados que deben repetirse. Prefiere una función conceptual `estado = f(tiempo, datos)`, una solución analítica, estados precalculados o una simulación reconstruible desde checkpoints.

## GSAP como coreografía

Una timeline GSAP puede expresar secuencias, solapamientos, pausas y cambios de propiedades. En HyperFrames, la skill oficial consultada describe timelines pausadas registradas por composición y controladas por la búsqueda del framework. Los IDs y el modo de registro deben coincidir con el contrato de la versión instalada.

`fromTo` ayuda a declarar ambos extremos de una transición y reduce dependencia de estilos dejados por búsquedas previas. No resuelve por sí solo todo problema de estado: una propiedad que CSS y GSAP modifican simultáneamente sigue teniendo control ambiguo. Cada propiedad animada debe tener una responsabilidad clara.

El easing comunica peso, precisión, urgencia o elasticidad. Escógelo por la causa perceptiva del movimiento; un easing llamativo aplicado a todo hace que los elementos compitan.

## Canvas, Three.js y eventos de seek

Para Canvas, Three.js u otro dibujo procedural, calcula la escena desde el tiempo solicitado y vuelve a dibujarla. La referencia de runtime oficial describe el evento `hf-seek` con el tiempo en el evento; confirma su disponibilidad y ciclo de vida en la versión actual antes de depender de él.

Una simulación dependiente de su estado anterior requiere reconstrucción: solución analítica, semilla y paso fijo, estados guardados o checkpoints. Aclara si una visualización es metáfora, ilustración o simulación técnica. No le atribuyas precisión física sin modelo y evidencia.

La etiqueta “Frame Adapter” y el evento `hf-seek` no son conceptos intercambiables automáticamente. El primero refiere a una interfaz de integración; el segundo a un mecanismo descrito por el runtime. Revisa documentación específica, no extrapoles soporte por parecido de nombres.

## Medios y propiedad de la reproducción

Deja al runtime administrar la visibilidad y la búsqueda de los elementos de audio/video que forman parte de la composición, según su contrato. Scripts que además llaman a `play()`, ajustan `currentTime` o sincronizan por reloj paralelo pueden competir con ese control.

Si el medio no responde a transformaciones durante el render, distingue el elemento de video del contenedor que se anima y confirma la solución con una muestra del render real.

## Diagnóstico por síntoma

| Síntoma | Hipótesis útil |
|---|---|
| El mismo instante se ve distinto según el recorrido | Estado acumulado, inicialización incompleta o aleatoriedad |
| Un objeto aparece en tiempo incorrecto | ID de timeline, reloj o ventana temporal no coincidente |
| Hay salto entre captura y preview | Recursos pendientes, fuentes, runtime o estado no reconstruible |
| Una propiedad parece luchar | CSS, GSAP o dos timelines controlan el mismo valor |
| Audio/video no sigue el seek | Control duplicado o contrato de medios incompatible |

Son hipótesis para orientar una inspección, no diagnósticos confirmados sin evidencia.

## Fuente y alcance

Síntesis del Libro E, capítulos 6–7; ver [GSAP Animation](https://hyperframes.app/docs/3-guides/3-gsap-animation), [Deterministic Rendering](https://hyperframes.app/docs/2-concepts/4-determinism), [Frame Adapters](https://hyperframes.app/docs/2-concepts/3-frame-adapters) y la referencia oficial de [runtimes](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/references/runtimes.md). Ejemplos conceptuales del libro no equivalen a una prueba de ejecución.
