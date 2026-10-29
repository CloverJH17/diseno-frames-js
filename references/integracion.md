# Arquitecturas: cómo se complementan los recursos

## Contenido

Capas; imágenes; video local; frameworks; integraciones; recursos; complejidad. Consulta [mapa](mapa-tecnologias.md) para elegir herramientas antes de diseñar conexiones.

## 1. Separar contenido, estilo y motor

Contenido contiene textos, cifras, recursos y fuentes. Estilo organiza paleta, familias, proporciones y carácter del movimiento. La escena relaciona objetos. El motor calcula estado, dibuja y captura. Esta separación permite cambiar un dato sin reescribir su geometría.

No toda pieza necesita una arquitectura extensible. Para una imagen única puede bastar un SVG limpio. Para una serie importan longitudes variables, referencias estables y componentes que admitan casos reales. Reutilización debe ahorrar trabajo sin congelar creatividad.

Los tokens preservan valores comunes, pero dos escenas con idénticos colores pueden verse incoherentes por proporciones, jerarquía y ritmo. Conserva también relaciones y límites de uso de componentes. Un sistema visual no es solamente un archivo de constantes.

## 2. Imagen SVG desde un modelo JS

Una función puede transformar datos en geometría: puntos, rutas, grupos y rótulos. La salida SVG conserva objetos editables. Si hay Canvas para previsualizar, comparte el modelo o verifica equivalencia; no lo presentes como vector exportable sin esa salida.

Antes de generalizar un generador, comprueba una pieza de máxima legibilidad. Luego prueba variaciones que realmente se usarán. El código debe servir al dibujo y al contenido, no imponer una familia de composiciones idénticas.

## 3. Motor local por tiempo

Una arquitectura posible es escena HTML/JS → navegador → captura → codificación audiovisual. Playwright puede controlar el navegador y FFmpeg procesar la secuencia. No es lo mismo que grabar pantalla en tiempo real: cada cuadro puede solicitarse por su instante.

La interfaz puede ser `seek(t)` en segundos o `renderFrame(f)` por índice. Debe reconstruir el estado completo, retornar cuando terminó el dibujo y esperar los recursos. No mezcles unidades ni supongas que cualquier HTML interactivo ya cumple ese contrato.

Captura y codificación pueden separarse. PNG preserva sin pérdida intermedia; JPEG reduce ciertos costos a cambio de pérdida. Una tubería evita miles de archivos pero exige comprobar cierre, salida y errores. El método no garantiza por sí mismo velocidad ni calidad superior.

## 4. Framework de composición

HyperFrames y Remotion pueden reducir trabajo de organización temporal y render. Sus contratos específicos se consultan cuando se elige el entorno. No mezcles atributos o APIs de versiones distintas por analogía.

Con React, el estado visual debe corresponder al fotograma. Con una timeline HTML, debe corresponder al tiempo que pide el motor. Una animación iniciada por reloj real puede verse bien en preview y quedar incorrecta en captura.

No introduzcas un framework excluido por el proyecto. Un índice general puede explicar sus ventajas sin convertirlo en dependencia obligatoria. Tampoco atribuyas a ese framework una producción ejecutada por otro camino.

## 5. Un reloj, varias superficies

DOM/SVG necesitan sus transformaciones; Canvas debe redibujarse; Three.js debe actualizar escena y renderizar; un shader recibe parámetros temporales; Lottie debe situarse en el fotograma correspondiente. Todo debe quedar listo antes de la captura.

Una timeline puede cambiar propiedades de objetos 3D, pero no sustituye la llamada de render del motor espacial. Un recurso Lottie necesita carga antes de buscar cuadros. Un video incrustado debe alcanzar el tiempo solicitado, no continuar reproduciéndose sin control.

No mantengas dos relojes compitiendo. Si el preview usa `requestAnimationFrame`, que invoque el mismo cálculo de estado y no mantenga una segunda versión de la lógica. La evaluación temporal debe ser verificable fuera del recorrido normal.

## 6. Recursos como parte de la reproducibilidad

La escena depende de fuentes, imágenes, modelos, audio y datos, además del código. Carga local estable o versiones fijadas reducen sorpresas; no instales ni descargues recursos ajenos al alcance autorizado.

Espera fuentes y decodificación de imágenes, incluyendo las que no aparecen como elementos DOM. En recursos asíncronos puede convenir una promesa de disponibilidad explícita. Falla con información útil ante un recurso esencial ausente; una alternativa tipográfica silenciosa puede cambiar toda la composición.

Registra procedencia y condiciones de uso donde corresponda. Un recurso de un catálogo externo no es automáticamente oficial, libre ni adecuado. Conserva activos de identidad originales e independientes de efectos.

## 7. Rendimiento y portabilidad

Más nodos, filtros, partículas, resolución y pasos de shader pueden elevar costo. Mide el cuello de botella real antes de simplificar todo. Transformaciones y opacidad pueden ser eficientes en ciertos contextos, pero no son gratuitas en todos los navegadores y escenas.

Un resultado determinista dentro de un entorno no implica identidad de píxel entre todas las GPU, sistemas y fuentes. Fija lo importante para repetir y declara el alcance. Un material o filtro puede necesitar prueba en el renderizador de entrega.

La mejor integración tiene pocas responsabilidades ambiguas. Si una biblioteca no resuelve una necesidad reconocible, considera retirarla. Complejidad útil permite una imagen que el contenido necesita; complejidad ornamental hace más frágil el mismo resultado.
