# Imágenes SVG y geometría editable

## Contenido

Qué significa vector; construcción; curvas; trazos y vacíos; texto; variantes; entrega. Complementa [fundamentos](fundamentos-visuales.md) y [dibujo procedural](ilustracion-procedural.md).

## 1. Definir la imagen necesaria

Una imagen puede ser SVG editable, composición HTML capturada, dibujo Canvas o salida de un modelo generativo. Aclara el original necesario si cambia el trabajo. Si se solicita vector, diseña geometría editable; un PNG incrustado en `image` no equivale a vectorización.

SVG puede contener fotografías, filtros y fuentes externas. Describe qué partes son trazados y cuáles dependen de otros recursos. Un archivo válido puede ser híbrido. El navegador no demuestra compatibilidad completa con cualquier editor ni aptitud para impresión o corte.

## 2. Construir antes de decorar

Empieza por silueta, proporciones y figura/fondo. Agrupa por significado: objeto, parte, sombra, detalle y rótulo. Las coordenadas locales facilitan modificar posición, escala o pose sin reescribir todo el dibujo.

El `viewBox` establece el sistema de coordenadas. Revisa relación de aspecto, límites y escalado. La caja debe contemplar trazos, extremos de curvas y filtros; los puntos centrales no representan toda la extensión visible.

Una figura orgánica se reconoce por estructura y gesto. Un ave necesita relaciones entre cabeza, pico, alas, cuerpo y postura; repetir plumas no corrige una silueta equivocada. Ordena estructura, contorno, planos y detalle selectivo. Revisa cada nivel antes de añadir el siguiente.

## 3. Bézier y continuidad

Los puntos de control expresan dirección y tensión. Usa pocos nodos en curvaturas simples y añade otros donde la forma cambia de función. Dos segmentos pueden coincidir en posición y mostrar un quiebre porque sus tangentes no acompañan el gesto.

Una esquina deliberada es distinta de un quiebre accidental. También revisa el cierre entre último y primer punto: puede introducir una punta inesperada. Examina ampliado para estudiar curvas y reducido para juzgar lectura. Ninguna escala sustituye la otra.

Las simetrías y repeticiones paramétricas ayudan a patrones y símbolos. Equilibrio óptico y alineación numérica no siempre coinciden. Ajusta masas sin romper relaciones que deban permanecer exactas.

## 4. Trazos, uniones y contraformas

Define una familia de grosores, terminales y uniones. Cambios arbitrarios entre redondo y recto producen piezas incompatibles. Un trazo fino desaparece al reducir; uno grueso cierra huecos. Comprueba ambos efectos al tamaño de uso.

Un agujero blanco no es transparencia. Las rutas compuestas con regla de relleno apropiada y las máscaras resuelven problemas diferentes según estructura. Comprueba vacíos sobre fondos claros, oscuros y de color. Conserva el `fill-rule` requerido en activos existentes.

`clipPath` delimita regiones geométricas; una máscara modula visibilidad mediante su contenido. Unidades, coordenadas y región de aplicación pueden cambiar al escalar. No son sustitutos universales. Revisa bordes y transparencias parciales.

La habilidad de generar trazados no autoriza redibujar un logo oficial. Importa el activo intacto y aplica transformaciones permitidas por el proyecto.

## 5. Gradientes, filtros y superficie

Un gradiente puede sugerir volumen o separar planos, pero necesita coherencia con la luz. No apliques el mismo brillo a materiales supuestamente distintos. Los filtros requieren región suficiente para no cortar sombras y desenfoques.

La evaluación de filtros utiliza superficies durante el render y puede variar entre herramientas. Si se exige geometría pura, edición por nodos o uso en fabricación, revisa los recursos permitidos. Apariencia correcta en pantalla y aptitud para producción específica son evidencias distintas.

## 6. Tipografía y significado de editable

Mantener `text` permite cambiar palabras si el destino dispone de la fuente y la interpreta. Convertir a curvas preserva silueta, pero permite editar nodos en lugar de texto. Conserva original textual si forma parte de la necesidad.

No recompongas un rótulo oficial trazado cuando debe permanecer intacto. En gráficos nuevos separa contenido de coordenadas: el dato no debería enterrarse en cientos de rutas. `title` y `desc` pueden aportar contexto accesible, sin sustituir una alternativa textual adecuada al uso.

## 7. Un modelo, varias salidas

Un modelo geométrico puede almacenar curvas, puntos, colores, rótulos y relaciones. Un exportador produce SVG; otro puede dibujar Canvas para previsualizar. Compartir datos evita que miniatura y original diverjan.

Esto requiere diseñar ambos recorridos; no es recuperación automática de vectores desde píxeles. El calco puede generar demasiados nodos y perder intención, grupos y semántica. Si se usa, necesita limpieza y revisión.

Una imagen tomada de una animación debe sostenerse como composición fija. El instante elegido puede tener texto incompleto o equilibrio que solo funciona por movimiento. Es legítimo recomponerla para su nuevo uso en lugar de declarar válida cualquier captura.

## 8. Variación controlada

Parametriza lo necesario: texto, proporción, paleta o detalle. No conviertas cada coordenada en una opción pública. Mantén relaciones: etiqueta separada del objeto, conectores apuntando a partes reales y zonas que admitan contenido variable.

Prueba extremos útiles si el sistema tendrá variantes: nombres largos, cifras cortas, fondo distinto y reducción. Para una pieza única, evita construir una fábrica de opciones sin necesidad.

## 9. Revisar y entregar

Abre el SVG final y la vista rasterizada. Comprueba referencias, IDs de máscaras, fuentes, recortes, filtros y alfa. Si importa otro editor, pruébalo allí cuando esté disponible. No prometas resultados universales por haber validado XML.

El PNG de vista previa ayuda a ver, pero no reemplaza el original vectorial solicitado. Explica diferencias de editabilidad, fuentes y recursos. Consulta [revisión](render-qc.md) para separar lo medido, lo observado y lo pendiente.
