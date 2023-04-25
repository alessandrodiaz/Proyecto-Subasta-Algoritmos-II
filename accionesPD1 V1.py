import copy


def accionesPD1(A, B, n, ofertas):
    solucionvalor = 0
    solucioncaminos = None
    A = int(A)
    matriz = {}
    caminos = {}
    numcompradores = n-1
    p_gov = ofertas[n-1][0]
    X = []  # array_solucion

    # Crear diccionario de valor por columnas->idcomprador->peso
    # Recorrer cada accion
    for i in range(1, A+1, 1):
        # Craer nueva "columna" (accion)
        matriz[i] = {}
        caminos[i] = {}

        # Recorrer cada comprador
        for j in range(0, numcompradores+1, 1):

            p = int(ofertas[j][0])
            c = int(ofertas[j][1])
            r = int(ofertas[j][2])
            idcomprador = j+1
            """
            Recorrer cada accion
            Recorrer cada comprador

            - - Si i es igual a algo entre el min y el max
            ---Restar i-
            """
            mejoropcion = 0.0
            # Si esta en el rango de acciones del comprador
            caminos[i][idcomprador] = {}

            if r <= i <= c:
                if i > r and i > 1:
                    # El comprador puede dar las acciones totales

                    capacidadrestante = 1

                    valoranteriornobasico = matriz[i-1][idcomprador]
                    compradores_valor_anterior = caminos[i-1][idcomprador]

                    valoranteriorbasico = (i-1)*p

                    valoractualbasico = p*i

                    max_columna = 0.0
                    nuevoscompradores = {}

                    for key_comp_externo, value in matriz[capacidadrestante].items():
                        p_comp_externo = float(ofertas[key_comp_externo-1][0])
                        c_comp_externo = int(ofertas[key_comp_externo-1][1])
                        r_comp_externo = int(ofertas[key_comp_externo-1][2])

                        # Si estoy en el rango de acciones que puede dar un externo
                        # No se toma en cuenta el camino del externo
                        # EXTERNO BASICO RESTANTE
                        if key_comp_externo != idcomprador and r_comp_externo <= capacidadrestante <= c_comp_externo:
                            if capacidadrestante*p_comp_externo > max_columna:
                                max_columna = capacidadrestante*p_comp_externo
                                nuevoscompradores[key_comp_externo] = capacidadrestante

                        # Si el comprador no esta en el camino de este comprador externo
                        # Si el externo no esta en el camino del previo del comprador
                        # EXTERNO NO BASICO and key_comp_externo not in compradores_valor_anterior and

                        if key_comp_externo != idcomprador and idcomprador not in caminos[capacidadrestante][key_comp_externo] and value > max_columna:
                            max_columna = value
                            nuevoscompradores = caminos[capacidadrestante][key_comp_externo]

                            # Comprador individual, valor alterno

                    # Valor anterior basico+externo basico restante
                    # Valor anterior basico+externo no basico restante
                    # Valor anterior no basico + externo basico restante
                    # Valor anterior no basico + externo no basico restante
                    # Valor actual basico SI
                    # Pueden haber valores anteriores del mismo comprador que sirvan?

                    max_columna += valoranteriorbasico

                    if max_columna > valoractualbasico:
                        caminos[i][idcomprador][idcomprador] = i-1
                        caminos[i][idcomprador].update(
                            compradores_valor_anterior)
                        caminos[i][idcomprador].update(nuevoscompradores)

                        matriz[i][idcomprador] = max_columna
                    else:
                        caminos[i][idcomprador][idcomprador] = i
                        matriz[i][idcomprador] = valoractualbasico

                    if matriz[i][idcomprador] > solucionvalor:
                        solucionvalor = matriz[i][idcomprador]
                        solucioncaminos = caminos[i][idcomprador]

                else:  # Si estamos en el minimo de acciones que compraria
                    caminos[i][idcomprador][idcomprador] = i
                    matriz[i][idcomprador] = i*p

                    if matriz[i][idcomprador] > solucionvalor:
                        solucionvalor = matriz[i][idcomprador]
                        solucioncaminos = caminos[i][idcomprador]
            elif i > c:
                capacidadrestante = i-c
                columnabuscar = matriz[capacidadrestante]
                max_columna = 0.0
                compradores = None
                nuevoscompradores = {}

                for key_comp_externo, beneficio in matriz[capacidadrestante].items():
                    if key_comp_externo != idcomprador and beneficio > max_columna and idcomprador not in caminos[capacidadrestante][key_comp_externo]:
                        max_columna = beneficio
                        nuevoscompradores = caminos[capacidadrestante][key_comp_externo]

                    p_comp_externo = float(ofertas[key_comp_externo-1][0])
                    c_comp_externo = int(ofertas[key_comp_externo-1][1])
                    r_comp_externo = int(ofertas[key_comp_externo-1][2])

                    if key_comp_externo != idcomprador and r_comp_externo <= capacidadrestante <= c_comp_externo:
                        if capacidadrestante*p_comp_externo > max_columna:
                            max_columna = capacidadrestante*p_comp_externo
                            nuevoscompradores[key_comp_externo] = capacidadrestante

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

    for key, value in matriz.items():
        print(key, ' : ', value)
    print("CAMINOS")
    for key, value in caminos.items():
        print(key, ' : ', value)
    return solucioncaminos, solucionvalor
    # print("------------")
    # print("MATRIZ-MATRIZ-MATRIZ-MATRIZ-MATRIZ-MATRIZ-MATRIZ-MATRIZ")
    # for key, value in matriz.items():
    # print(key, ' : ', value)
    # print("CAMINOS")
    # for key, value in caminos.items():
    # print(key, ' : ', value)

    # for key, value in caminos.items():
    # print(key, ' : ', value)
    # Llenar datos de la matriz
    numcolumnas = int(A)

    # Necesito comparar la capacidad actual con TODOS LOS ITEM, restarlos
    # ahora buscar en la capacidadrestante el que me sirve

    # for key, value in matriz.items():
    #     if key >=
    #     print()

    # Todos los items
    items = matriz.copy()

    # Vamos guardando el mejor precio de la matriz
    mejorpreciofinal = 0
    posicionj = None
    posicioni = None
    """
    # Recorremos el diccionario de columnas desde la llave (columna) 2
    for i in range(0, len(matriz)+1, 1):
        print(i, len(matriz))
        # COLUMNA 4, COMPRADOR 1-COMPRADOR2
        # Empezamos a mirar desde la columna 2
        # if i > 1:
        for keycolumna, valuecolumna in items.items():
            # Si el peso cabe en la capacidad
            for keycomprador, valuecomprador in valuecolumna.items():
                for keypeso, valuepeso in valuecomprador.items():
                    if keypeso < i:
                        # print("columna", i, "comprador",
                        # keycomprador, "peso", keypeso)
                        capacidadrestante = i-keypeso
                        beneficio = valuepeso
                        # print("restante", capacidadrestante,
                        # "beneficio", beneficio)
                        # print(capacidadrestante)
                        mejoropcion = 0
                        if capacidadrestante > 0:
                            columnabusqueda = matriz[capacidadrestante]
                            # print("busca->", columnabusqueda)

                            for keycomprador2, valuecomprador2 in columnabusqueda.items():
                                if keycomprador2 != keycomprador:
                                    for keypeso2, valuepeso2 in valuecomprador2.items():
                                        if valuepeso2 > mejoropcion:
                                            # print("value", valuepeso2)
                                            mejoropcion = valuepeso2
                                            # print(
                                            # "Column", columnabusqueda)
                                            compradoresprevios = caminos[capacidadrestante]
                                            # print(caminos[1][1][1])
                                            # print(compradoresprevios)

                                            beneficio += valuepeso2

                                            # print(
                                            # "1->", matriz[i], keycomprador)
                                            # matriz[i][keycomprador] = {}
                                            # print(
                                            # "2->", matriz[i], keycomprador)
                                            # matriz[i][keycomprador] = {}
                                            if keycomprador not in matriz[i]:
                                                matriz[i][keycomprador] = {}

                                            matriz[i][keycomprador][keypeso] = beneficio

                                            # print(matriz[i][keycomprador][i])

                            # print(columnabusqueda)


    print("CAMINOS-CAMINOS-CAMINOS-CAMINOS-CAMINOS-CAMINOS")
    for key, value in caminos.items():
        print(key, ' : ', value)
    """
    """
    # Recorrer de izquierda a derecha la matriz
    for i in range(0, numcolumnas + 1, 1):

        # print(i, numcolumnas)

        # Recorrer cada columna
        for j in range(0, len(matriz), 1):

            mejoropcion = 0

            # Si coincide (diagonal)
            if i < int(A):
                matriz[j].append(0)
                caminos[j].append([])

            if i > 0:
                if i == (matriz[j][0][0]):
                    matriz[j][i] = matriz[j][0][1]
                    caminos[j][i].append(matriz[j][0][2])
                    caminos[j][i].append([matriz[j][0][0]])

            # Empezamos a hacer calculos desde la accion (columna) 2
            if i > 1:
                comprador = 0
                compradores = []
                columna = i
                # La capacidad restante es el num de la columna (capacidad) menos el peso del item
                capacidadrestante = columna - matriz[j][0][0]

                if capacidadrestante > 0:
                    # Cual es el valor mas alto de la columna indicada
                    for k in range(0, len(matriz), 1):
                        # Si el elemento actual no es del mismo comprador, Si el comprador no esta en el camino
                        if matriz[k][capacidadrestante] > mejoropcion and matriz[k][0][2] != matriz[j][0][2] and matriz[j][0][2] not in caminos[k][capacidadrestante]:
                            compradores = []
                            comprador = 0

                            # Tomamos beneficio de la mejor opcion
                            mejoropcion = matriz[k][capacidadrestante]

                            # Tomamos id del comprador actual
                            comprador = copy.copy(matriz[j][0][2])

                            # Tomamos los caminos previos de la mejor opcion
                            compradores = copy.copy(
                                caminos[k][capacidadrestante])

                    if mejoropcion > 0:

                        beneficio = mejoropcion + matriz[j][0][1]
                        matriz[j][i] = beneficio

                        # Guardamos el mejor precio hasta el momento
                        if beneficio > mejorpreciofinal:
                            mejorpreciofinal = beneficio
                            posicioni = i
                            posicionj = j

                        compradores.insert(0, comprador)
                        caminos[j][i] = compradores
                        # Insertamos el num de acciones del comprador nuevo
                        caminos[j][i].insert(
                            int(len(caminos[j][i]) / 2) + 1, [matriz[j][0][0]])

    for i in range(len(matriz)):
        print(matriz[i])


  IMPRESION RESPUESTA -----------------


    respuesta = caminos[posicionj][posicioni]
    ncompradores = len(respuesta) / 2
    accionesvendidas = 0

    for i in range(1, numcompradores + 1, 1):
        if int(i) not in caminos[posicionj][posicioni]:
            X.append(0)
        else:
            indice = respuesta.index(i) + int(ncompradores)
            acciones = respuesta[indice][0]
            accionesvendidas += acciones
            X.append(acciones)


    # Acciones gobierno
    mejorpreciofinal += (A - accionesvendidas) * p_gov
    X.append(A - accionesvendidas)

    return X, mejorpreciofinal
    """
