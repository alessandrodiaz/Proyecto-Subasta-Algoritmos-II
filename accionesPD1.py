
def accionesPD1(A, B, n, ofertas):
    solucionvalor = 0
    solucioncaminos = None
    A = int(A)
    matriz = {}
    caminos = {}
    numcompradores = n
    p_gov = ofertas[n-1][0]

    # Crear diccionario de valor por columnas->idcomprador->peso
    # Recorrer cada accion
    i = 1
    continuar = True
    while continuar:
        # print(i)
        # Craer nueva "columna" (accion)
        matriz[i] = {}
        caminos[i] = {}

        # Recorrer cada comprador
        for j in range(0, numcompradores, 1):

            p = int(ofertas[j][0])
            c = int(ofertas[j][1])
            r = int(ofertas[j][2])
            idcomprador = j+1
            caminos[i][idcomprador] = {}

            if i <= A:
                if r <= i <= c:
                    matriz[i][idcomprador] = i*p
                    caminos[i][idcomprador][idcomprador] = i

                    if matriz[i][idcomprador] > solucionvalor:
                        solucionvalor = matriz[i][idcomprador]
                        solucioncaminos = caminos[i][idcomprador]
                elif i > c:
                    capacidadrestante = i-c
                    max_columna = 0.0
                    nuevoscompradores = {}

                    for key_comp_externo, beneficio in matriz[capacidadrestante].items():
                        if key_comp_externo != idcomprador and beneficio > max_columna and idcomprador not in caminos[capacidadrestante][key_comp_externo]:
                            max_columna = beneficio
                            nuevoscompradores = caminos[capacidadrestante][key_comp_externo]

                    if max_columna > 0:
                        caminos[i][idcomprador][idcomprador] = c
                        caminos[i][idcomprador].update(nuevoscompradores)
                        matriz[i][idcomprador] = max_columna+c*p
                    else:
                        caminos[i][idcomprador][idcomprador] = c
                        matriz[i][idcomprador] = c*p

                    if matriz[i][idcomprador] > solucionvalor:
                        solucionvalor = matriz[i][idcomprador]
                        solucioncaminos = caminos[i][idcomprador]
            else:
                accion_revisar = i-A
                accion_revisar = c-accion_revisar

                if accion_revisar >= r:
                    capacidadrestante = A-accion_revisar
                    max_columna = 0.0
                    nuevoscompradores = {}

                    for key_comp_externo, beneficio in matriz[capacidadrestante].items():
                        if key_comp_externo != idcomprador and beneficio > max_columna and idcomprador not in caminos[capacidadrestante][key_comp_externo]:
                            max_columna = beneficio
                            nuevoscompradores = caminos[capacidadrestante][key_comp_externo]

                    if max_columna > 0:
                        caminos[i][idcomprador][idcomprador] = accion_revisar
                        caminos[i][idcomprador].update(nuevoscompradores)
                        matriz[i][idcomprador] = max_columna+accion_revisar*p
                    else:
                        caminos[i][idcomprador][idcomprador] = accion_revisar
                        matriz[i][idcomprador] = accion_revisar*p

                    if matriz[i][idcomprador] > solucionvalor:
                        solucionvalor = matriz[i][idcomprador]
                        solucioncaminos = caminos[i][idcomprador]
                elif (j+1) == numcompradores:
                    continuar = False

        i += 1

    # Impresion
    # for key, value in matriz.items():
    #     print(key, ' : ', value)
    # print("CAMINOS")
    # for key, value in caminos.items():
    #     print(key, ' : ', value)

    arraysolucion = []
    accionesvendidas = 0

    for i in range(1, numcompradores+1, 1):
        if i in solucioncaminos:
            accionesvendidas += solucioncaminos[i]
            arraysolucion.append(solucioncaminos[i])
        else:
            arraysolucion.append(0)

    return arraysolucion, solucionvalor
