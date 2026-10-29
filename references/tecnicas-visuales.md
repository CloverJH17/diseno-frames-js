# Tiempo, movimiento y continuidad

## Contenido

Relojes; interpolación; coreografía; tipografía; cámara; transiciones; fallos. Los fundamentos son generales; las fórmulas ilustran mecanismos, no duraciones ni estilos obligatorios.

## 1. Cuatro tiempos relacionados

Tiempo narrativo entrega información; tiempo cinético transforma propiedades; tiempo musical organiza acentos; tiempo técnico indexa cuadros. Pueden dialogar sin coincidir en cada golpe. Ningún BPM sustituye el tiempo que una frase necesita para leerse.

Define `I(t)=F(escena, datos, estilo, semilla, t)`. Para `N` cuadros a frecuencia `fps`, muestrea `t=f/fps`, con `f=0..N-1`; la duración efectiva es `N/fps`. Si la duración deseada no produce N entero, decide redondeo y registra su consecuencia. No añadas automáticamente un cuadro en t final.

Calcula estado completo desde tiempo absoluto. Evita `x += velocidad`, reloj real y azar por cuadro en la ruta exportable. Para física usa solución analítica, simulación precalculada o estados reproducibles. Una prueba A→B→A detecta algunos residuos de estado, no todos los fallos posibles.

## 2. Interpolación y carácter

Interpolar calcula valores intermedios; easing cambia el progreso. Separar ambos permite cambiar sensación sin cambiar destino.

```js
const clamp01 = u => Math.max(0, Math.min(1, u));
const lerp = (a, b, u) => a + (b - a) * u;
const smooth = u => { u = clamp01(u); return u*u*(3-2*u); };
const outCubic = u => 1 - (1-clamp01(u))**3;
```

Estas expresiones no necesitan una biblioteca. `smooth` suaviza extremos; `outCubic` avanza pronto y se asienta. Un objeto pesado, una letra y una chispa pueden requerir duraciones y curvas diferentes. No existe una curva universalmente profesional.

Anticipación prepara; acción entrega; asentamiento confirma. Overshoot puede expresar elasticidad o torpeza según escala y contexto. El movimiento secundario debe apoyar el gesto principal. No apliques rebote a todos los objetos porque esté disponible.

## 3. Coreografía y quietud

Diseña estados reconocibles: presentación, transformación, resultado y retención. Un protagonista puede ocupar primero una composición completa y desplazarse cuando llega información nueva; reservar huecos largos puede quitar fuerza al inicio.

Un foco por momento no significa un solo objeto. Significa una relación clara entre acción principal, respuestas y ambiente. Escalonar demasiado vuelve lenta una secuencia; hacerlo demasiado poco produce competencia. Varía puesta en escena sin perder personalidad cinética.

En GSAP organiza la timeline desde estados iniciales claros y un reloj externo. DOM, SVG, Canvas y Three.js deben reflejar ese tiempo antes de capturar. Evita que callbacks acumulativos o transiciones CSS sigan alterando la escena después de solicitar el estado.

## 4. Texto que actúa

Anima por palabra, línea o grupo semántico según intención. Por carácter puede aportar gesto, pero retrasa la lectura y puede romper percepción de palabras. Conserva signos, espacios, acentos y grupos de grafemas cuando se separa texto.

Mide con la fuente cargada; ancho fijo por letra destruye espaciado. Incluso sumar avances individuales puede perder kerning o ligaduras: revisa la palabra compuesta y el nivel de separación apropiado. En Canvas compara medición y silueta; en DOM revisa glifos transformados, no solo cajas.

Con n elementos, retraso d y duración e, el último termina en `inicio+(n-1)*d+e`. Después necesita permanencia antes de la salida. Esa fórmula explica por qué una lista puede desaparecer sin llegar a construirse aunque su ventana total parezca suficiente.

Titular, apoyo y captions tienen funciones distintas. Repetir la misma oración tres veces aumenta densidad sin añadir comprensión. Reserva zonas o alterna tiempos para que no se tapen.

## 5. Cámara, escala y profundidad

Un zoom debe descubrir detalle o cambiar significado, no sustituir una acción ausente. En 2D piensa en traslación y escala alrededor de un anclaje coherente; en 3D, en perspectiva, posición y objetivo. Evita saltos de anclaje cuando un objeto cambia de tamaño.

El paralaje relaciona planos. Diferencias moderadas pueden crear profundidad; exceso desplaza la atención y provoca incomodidad. En 3D comprueba oclusiones y lectura; perspectiva dramática puede deformar cifras y etiquetas.

## 6. Transición como relación

Diseña salida y entrada juntas. Un corte puede expresar claridad; un fundido, coexistencia; una transformación, continuidad de concepto. La transición no debe elegirse solo por lo vistoso de su nombre.

Un fundido matemáticamente suave puede superponer titulares ilegibles. Cambia orden, zonas o tipo de transición. En un barrido opaco revela el fondo entrante completo, con sus planos y pie, para evitar un salto al terminar la máscara.

En un barrido circular calcula cobertura hasta la esquina más lejana desde su origen. No consumas la animación entrante mientras todavía está oculta si luego no queda lectura. Revisa antes, durante y después de la unión, incluyendo cuadros vecinos al límite.

Morphing requiere correspondencia de forma y control de estados intermedios. Dos rutas válidas pueden producir una silueta irreconocible a mitad. Una transformación de logo solo procede si las reglas de identidad permiten modificarlo; una máscara sobre el archivo intacto es otra operación.

## 7. Diagnóstico de fallos transferibles

| Síntoma | Hipótesis | Corrección a comprobar |
|---|---|---|
| Último elemento nunca termina | Entrada excede salida | Recalcular entrada y permanencia |
| Tarjetas se cruzan con texto legible | Transformación mezcla funciones | Retirar texto antes; usar formas simples |
| Paisaje aparece de golpe | Máscara revela solo color plano | Revelar fondo completo |
| Captions tapan información | Misma zona y alturas variables | Alternar o separar funciones |
| Forma cambia tras retroceder | Estado acumulado | Reconstrucción temporal y prueba A→B→A |
| Todo parece una misma plantilla | Gesto y composición repetidos | Variar estructura según contenido |

Comprueba la hipótesis en la pieza. Estos patrones provienen de experiencias de producción, no garantizan una causa única para cualquier fallo. Véase [revisión](render-qc.md) y [sonido](sonido-sincronia.md).
