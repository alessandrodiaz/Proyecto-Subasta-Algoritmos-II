import copy


def accionesPD2(A, B, n, ofertas):
    matriz = []
    caminos = []
    numcompradores = n
    p_gov = ofertas[n][0]
    tam_paq = ofertas[n][2]
    X = []  # array_solucion

    # Recorrer cada comprador
    for i in range(0, numcompradores, 1):

        p = int(ofertas[i][0])
        c = int(ofertas[i][1])
        r = int(ofertas[i][2])
        accionactual = r

        # Crear cada posible accion en la matriz
        for j in range(r, c + 1, tam_paq):
            beneficio = j * p
            fila = [[j, beneficio, i + 1]]
            #filacaminos = [[j, beneficio, i + 1]]

            matriz.append(fila)
            caminos.append(fila.copy())  # changed
            accionactual += 1

    # Llenar datos de la matriz
    numcolumnas = int(A)
    # Vamos guardando el mejor precio de la matriz
    mejorpreciofinal = 0
    posicionj = None
    posicioni = None

    # Recorrer de izquierda a derecha la matriz
    iteracion = 0
    for i in range(0, numcolumnas + tam_paq, tam_paq):

        # Recorrer cada columna
        for j in range(0, len(matriz), 1):

            indice_columna = int(i / tam_paq)
            mejoropcion = 0

            # Si coincide (diagonal)
            if i < int(A):
                matriz[j].append(0)
                caminos[j].append([])

            if i > 0:
                if i == (matriz[j][0][0]):
                    matriz[j][iteracion] = matriz[j][0][1]
                    caminos[j][iteracion].append(matriz[j][0][2])
                    caminos[j][iteracion].append([matriz[j][0][0]])

            # Empezamos a hacer calculos desde la (columna) 2
            if i > 1:
                comprador = 0
                compradores = []
                columna = i
                # La capacidad restante es el num de la columna (capacidad) menos el peso del item
                capacidadrestante = columna - matriz[j][0][0]
                indice_columna_busqueda = int(capacidadrestante / tam_paq)

                if capacidadrestante > 0:
                    # Cual es el valor mas alto de la columna indicada
                    for k in range(0, len(matriz), 1):

                        if matriz[k][indice_columna_busqueda] > mejoropcion:
                            # Si el elemento actual no es del mismo comprador
                            if matriz[k][0][2] != matriz[j][0][2]:
                                # Si el comprador no esta en el camino
                                if matriz[j][0][2] not in caminos[k][indice_columna_busqueda]:
                                    compradores = []
                                    comprador = 0

                                    # Tomamos beneficio de la mejor opcion
                                    mejoropcion = matriz[k][indice_columna_busqueda]

                                    # Tomamos id del comprador actual
                                    comprador = copy.copy(matriz[j][0][2])

                                    # Tomamos los caminos previos de la mejor opcion
                                    compradores = copy.copy(
                                        caminos[k][indice_columna_busqueda])

                    if mejoropcion > 0:

                        beneficio = mejoropcion + matriz[j][0][1]

                        indice_columna = int(i / tam_paq)
                        matriz[j][indice_columna] = beneficio

                        # Guardamos el mejor precio hasta el momento
                        if beneficio > mejorpreciofinal:
                            mejorpreciofinal = beneficio
                            posicioni = indice_columna
                            posicionj = j

                        compradores.insert(0, comprador)
                        caminos[j][indice_columna] = compradores
                        # Insertamos el num de acciones del comprador nuevo
                        caminos[j][indice_columna].insert(
                            int(len(caminos[j][indice_columna]) / 2) + 1, [matriz[j][0][0]])

        iteracion += 1

    for i in range(len(matriz)):
        print(matriz[i])

    """
  IMPRESION RESPUESTA -----------------
  """

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
    print(X, mejorpreciofinal)

    return X, mejorpreciofinal
