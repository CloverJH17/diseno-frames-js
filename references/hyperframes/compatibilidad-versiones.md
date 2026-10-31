# Compatibilidad de HyperFrames por versión

## Por qué existe esta nota

La documentación y las skills evolucionan a ritmos diferentes. Una página pública, una skill en la rama principal, el paquete local y una versión fijada en un proyecto pueden describir contratos distintos. No conviertas una captura fechada en una verdad permanente.

## Registro de la auditoría del 29 de octubre de 2026

La investigación del Libro E comparó documentación pública de HyperFrames con skills oficiales accesibles en la fecha indicada. La skill oficial consultada estaba en el commit `f7db6ba40cb2f95390513dc76ad0a9e83b490673` (referencia fechada de la auditoría; no implica que siga siendo la versión actual).

| Tema | Referencia pública consultada | Skill oficial consultada | Tratamiento prudente |
|---|---|---|---|
| Duración total | Atribuye papel a la duración de la timeline GSAP y dice que `data-duration` no se usa en composiciones | Declara `data-duration` en la raíz como duración de la película | Verifica esquema y timeline del paquete/versión del proyecto; no infieras duración desde GSAP |
| Índice de pista | Algunas páginas lo describen como orden visual | La skill/format indica fila de Studio; el orden de pintura se resuelve con CSS/z-index | Comprueba estructura y captura con elementos solapados |
| Timeline anidada | Semántica de pausa descrita de forma distinta entre páginas | Las referencias oficiales actuales de la auditoría detallan otro contrato | Aísla una composición anidada y valida seeking en versión fijada |
| Canvas y 3D | Frame Adapters se presenta como API v0 experimental con integraciones marcadas como planificadas | La skill de runtime describe el protocolo de evento `hf-seek` | No equipares adaptador formal y listener de runtime; verifica API concreta |

Este registro comunica una discrepancia documental observada en una fecha y revisión determinadas; no declara cuál conducta prevalece en cualquier instalación. Los enlaces pueden cambiar después de la fecha de auditoría.

## Procedimiento de compatibilidad

1. Identifica la versión de HyperFrames y sus dependencias en el proyecto real.
2. Consulta la ayuda local y las referencias instaladas que correspondan a esa versión.
3. Compara con documentación primaria fechada y fija los supuestos relevantes del proyecto.
4. Crea la comprobación mínima pertinente: duración, solapamiento, nested composition, seek o medio afectado.
5. Guarda la evidencia y anota qué versión probaste; separa capacidad documentada, implementación observada e hipótesis.
6. Revisa esta tabla cuando cambie la versión, el contrato local o las fuentes.

No actualices automáticamente el paquete, descargues modelos, instales skills ni actives proveedores para resolver una duda de compatibilidad. Primero decide qué comprobación puede realizarse con los recursos existentes.

## Fuentes de la auditoría

- [Data Attributes](https://hyperframes.app/docs/2-concepts/2-data-attributes)
- [Frame Adapters](https://hyperframes.app/docs/2-concepts/3-frame-adapters)
- [Skill oficial principal, commit fijado](https://github.com/heygen-com/hyperframes/blob/f7db6ba40cb2f95390513dc76ad0a9e83b490673/skills/hyperframes/SKILL.md)
- [Referencia oficial de formato, commit fijado](https://github.com/heygen-com/hyperframes/blob/f7db6ba40cb2f95390513dc76ad0a9e83b490673/skills/hyperframes/references/format.md)
- [Referencia oficial de runtimes, commit fijado](https://github.com/heygen-com/hyperframes/blob/f7db6ba40cb2f95390513dc76ad0a9e83b490673/skills/hyperframes/references/runtimes.md)

## Alcance de la edición

La observación proviene del Libro E y de fuentes consultadas el 29 de octubre de 2026. No se instaló HyperFrames, no se ejecutó un render, no se probó una composición anidada y no se modificó el repositorio público durante esa auditoría. Los diagnósticos anteriores a una prueba local permanecen como asuntos por verificar.
