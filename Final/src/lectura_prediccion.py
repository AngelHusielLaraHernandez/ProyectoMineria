"""Texto de interpretación para cada consulta de popularidad."""


def concluir_prediccion(fila, nivel, probabilidades, notas_entrenamiento):
    orden = sorted(probabilidades, key=probabilidades.get, reverse=True)
    alternativa = next(clase for clase in orden if clase != nivel)
    ganador = probabilidades[nivel]
    siguiente = probabilidades[alternativa]
    margen = (ganador - siguiente) * 100
    if margen < 0.05:
        lectura = (
            f'Los niveles **{nivel}** ({ganador:.1%}) y **{alternativa}** ({siguiente:.1%}) '
            'quedaron prácticamente empatados.'
        )
    else:
        lectura = (
            f'El nivel **{nivel}** quedó primero con **{ganador:.1%}**. '
            f'Le sigue **{alternativa}** con **{siguiente:.1%}**, a **{margen:.1f} puntos porcentuales**.'
        )
    if ganador < 0.5:
        lectura += ' Los otros dos niveles reúnen en conjunto más probabilidad.'

    generos = ', '.join(fila['generos'])
    organizaciones = fila['estudio']
    estudio = ', '.join(organizaciones) if organizaciones and organizaciones != ['Otro'] else 'organización no especificada o poco frecuente'
    decada = f'década de {int(fila["decada"])}' if fila['decada'] >= 0 else 'década desconocida'
    if fila['Metacritic Rating'] != fila['Metacritic Rating']:
        prensa = f'la nota de prensa se estimó con la mediana del entrenamiento ({notas_entrenamiento:g}/100)'
    else:
        prensa = f'la nota de prensa fue {fila["Metacritic Rating"]:g}/100'
    contexto = (
        f'La consulta combina {generos}, {estudio} y {decada}. '
        f'La nota de usuarios fue {fila["Rating"]:g}/5 y {prensa}.'
    )
    return lectura, contexto
