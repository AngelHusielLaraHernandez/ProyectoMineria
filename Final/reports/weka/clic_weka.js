// Control gráfico local de Weka; autorizado expresamente por el usuario.
ObjC.import('ApplicationServices');
function run(argumentos) {
    if (argumentos.length < 2 || argumentos.length > 3) throw new Error('Indica x, y y opcionalmente la ventana de Weka.');
    var nombreVentana = argumentos.length === 3 ? argumentos[2] : 'Weka Explorer';
    var permitidas = ['Weka Explorer', 'Package Manager', 'Weka Package Manager', 'weka.gui.GenericObjectEditor', 'Weka GUI Chooser', 'Abrir'];
    if (permitidas.indexOf(nombreVentana) < 0) throw new Error('Ventana fuera del alcance autorizado de Weka.');
    var x = Number(argumentos[0]);
    var y = Number(argumentos[1]);
    var sistema = Application('System Events');
    var proceso = sistema.processes.byName('weka-3.8.7');
    var ventana = proceso.windows.byName(nombreVentana);
    var posicion = ventana.position();
    var tamano = ventana.size();
    if (!Number.isFinite(x) || !Number.isFinite(y) ||
        x < posicion[0] || x >= posicion[0] + tamano[0] ||
        y < posicion[1] || y >= posicion[1] + tamano[1]) {
        throw new Error('El clic debe quedar dentro de la ventana autorizada de Weka.');
    }
    proceso.frontmost = true;
    delay(0.3);
    var punto = $.CGPointMake(x, y);
    var pulsar = $.CGEventCreateMouseEvent(null, $.kCGEventLeftMouseDown, punto, $.kCGMouseButtonLeft);
    var soltar = $.CGEventCreateMouseEvent(null, $.kCGEventLeftMouseUp, punto, $.kCGMouseButtonLeft);
    $.CGEventSetIntegerValueField(pulsar, $.kCGMouseEventClickState, 1);
    $.CGEventSetIntegerValueField(soltar, $.kCGMouseEventClickState, 1);
    $.CGEventPost($.kCGHIDEventTap, pulsar);
    $.CGEventPost($.kCGHIDEventTap, soltar);
    return 'Clic gráfico enviado dentro de la ventana autorizada de Weka.';
}
