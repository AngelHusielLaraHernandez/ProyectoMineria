// Lectura de accesibilidad limitada al proceso Weka autorizado.
ObjC.import('ApplicationServices');
function atributo(elemento, nombre) {
    var salida = Ref();
    var codigo = $.AXUIElementCopyAttributeValue(elemento, $(nombre), salida);
    return codigo === 0 ? salida[0] : null;
}
function cadena(valor) {
    if (valor === null) return '';
    try { return ObjC.unwrap(valor); } catch (e) { return ''; }
}
function recorrer(elemento, profundidad, salida) {
    if (profundidad > 12 || salida.length > 500) return;
    var rol = cadena(atributo(elemento, 'AXRole'));
    var titulo = cadena(atributo(elemento, 'AXTitle'));
    var descripcion = cadena(atributo(elemento, 'AXDescription'));
    var valor = cadena(atributo(elemento, 'AXValue'));
    salida.push({nivel: profundidad, rol: rol, titulo: titulo, descripcion: descripcion, valor: valor});
    var hijos = atributo(elemento, 'AXChildren');
    if (hijos) {
        for (var i = 0; i < Number(hijos.count); i++) recorrer(hijos.objectAtIndex(i), profundidad + 1, salida);
    }
}
function run() {
    var proceso = Application('System Events').processes.byName('weka-3.8.7');
    var sistema = Application('System Events');
    proceso.frontmost = true;
    delay(0.2);
    sistema.keyCode(53);
    var boton = proceso.windows.byName('Weka Explorer').tabGroups[0].buttons.whose({description: 'Choose'})[0];
    boton.attributes.byName('AXFocused').value = true;
    sistema.keyCode(49);
    delay(0.3);
    var aplicacion = $.AXUIElementCreateApplication(proceso.unixId());
    var ventanas = atributo(aplicacion, 'AXWindows');
    var salida = [];
    for (var i = 0; i < Number(ventanas.count); i++) {
        var ventana = ventanas.objectAtIndex(i);
        if (cadena(atributo(ventana, 'AXTitle')) === '') recorrer(ventana, 0, salida);
    }
    return JSON.stringify(salida, null, 2);
}
