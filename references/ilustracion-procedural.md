# Ilustración procedural: código como lenguaje de dibujo

## Contenido

Gramática visual; Canvas; p5.js; variación; paisajes; personajes; profundidad y shaders. Complementa [SVG](svg-imagenes.md) y [movimiento](tecnicas-visuales.md).

## Una gramática, no una colección de primitivas

Las primitivas geométricas son bloques. La calidad aparece en relaciones: proporción, gesto, contorno, luz, densidad y detalle. Un árbol puede surgir de ramificaciones; una ciudad, de proporciones entre calles y fachadas; un personaje, de articulaciones y masas.

Define qué varía y qué permanece. En edificios pueden cambiar altura y ventanas sin variar perspectiva y luz. Si todo cambia sin límites desaparece el estilo; si nada cambia aparece repetición mecánica.

El algoritmo debe expresar observación visual. Una nube tiene masa, bordes y agrupación; ruido repartido por pantalla no basta. Para lluvia importan dirección, longitudes, profundidad y zonas iluminadas, además de cantidad.

## Canvas y control de superficie

Canvas facilita curvas, capas, imágenes y texto en orden explícito. Conserva un modelo separado si necesitas objetos seleccionables o cajas para revisión. El lienzo no mantiene por sí mismo un nodo por cada forma dibujada.

Aísla transformaciones, recortes, opacidad y sombras con estados locales. Una transformación no restaurada deforma capas posteriores; un alpha heredado puede volver ilegible el cierre. Reconstruye la superficie para cada estado exportable. Si la acumulación de trazos es intencional, debe poder reproducirse.

Distingue resolución lógica, presentación y captura. Ampliar un lienzo pequeño no añade detalle. Para nitidez alta calcula a resolución adecuada o usa modelo vectorial. El rendimiento puede justificar un compromiso, pero debe describirse con claridad.

## p5.js como laboratorio

p5.js reduce fricción al explorar geometría, color, ruido y transformaciones. Su bucle habitual favorece interacción; un video exportable necesita reconstrucción por tiempo. Adaptar un sketch interactivo exige revisar esas dependencias.

Una semilla no basta si el número de llamadas aleatorias depende de cuántos cuadros pasaron. Precalcula atributos, deriva valores de identificadores estables o guarda estados necesarios. El mismo problema afecta simulaciones y ruido usados de forma acumulativa.

La salida habitual de `saveCanvas` es raster. Un SVG requiere una representación y exportador compatibles revisados. No prometas que cualquier sketch se convierte conservando capas. Elige p5.js por su aporte creativo concreto.

## Variación con distribución

Un bosque puede tener grupos, claros y cambios de escala con distancia. El azar uniforme suele dispersar detalles y quitar foco. Controla exclusiones alrededor de textos, gradientes de densidad y tamaños vinculados al plano.

Ruido correlacionado ofrece continuidad; azar independiente produce saltos. Una trayectoria de viento suele necesitar suavidad; una textura puede admitir irregularidad local. Amplitud y frecuencia deben corresponder al tamaño y función del objeto.

Conserva atributos estables y anima lo necesario. Una hoja que cambia aleatoriamente de silueta cada cuadro parece fallar, no moverse con viento. Organicidad suele requerir menos variación de la esperada.

## Paisaje y cámara

Organiza profundidad con superposición, escala, valor y detalle. Lo lejano puede simplificarse; lo cercano puede ganar contraste. Son recursos expresivos, no leyes obligatorias para toda estética. Define horizonte y perspectiva antes de repartir objetos.

La cámara debe revelar relaciones. Revisa coherencia del paralaje, bordes descubiertos y continuidad espacial en todo el recorrido. Un paisaje convincente en un encuadre puede romperse al desplazarse.

Un escenario conceptual no representa automáticamente una localidad real. Mapas y obras específicas requieren fuentes. Añadir un rótulo no convierte una ilustración inventada en evidencia territorial.

## Personajes y articulación

Define torso, cabeza, extremidades, puntos de giro y solapamientos. La postura debe leerse en silueta. Un punto de rotación accidental puede hacer que una mano flote o se separe del cuerpo.

Una figura fija no está necesariamente preparada para animación. Manos pueden requerir varias poses; una cara, cambios de contorno; un ala, un gesto completo. Empieza por una acción legible antes de construir una biblioteca de movimientos.

La ilustración procedural no autoriza modificar mascotas oficiales. Sus reglas y permisos siguen perteneciendo al proyecto.

## Superficie y GPU

Los planos 2D sugieren profundidad. Si necesitas oclusiones y luz espacial coherente, una escena Three.js puede ser apropiada. El costo debe corresponder a la información que añade.

Shaders sirven para ondas, ruido, disolución y luz estilizada. Diseña frecuencia, amplitud, contraste y región de aplicación. Mantén tipografía estable cuando la distorsión dificulta leer. SDF describe distancias a formas; ray marching puede aprovecharlas para representar volumen. Son posibilidades, no pasos obligatorios hacia calidad.

## Revisar el sistema y su imagen

Si habrá variantes, prueba varias semillas y contenidos. Comprueba foco, densidad y colisiones. Un sistema flexible puede producir un ejemplo excelente y otros inutilizables. Para una pieza única fija una configuración que funcione; para una familia define límites.

Juzga el resultado visible. Cantidad de código, partículas y complejidad matemática no miden calidad artística. La [revisión](render-qc.md) debe estudiar tanto el modelo como su salida final.
