import copy


def accionesPD1(A, B, n, ofertas):
    matriz = []
    caminos = []
    numcompradores = n-1
    p_gov = ofertas[n-1][0]
    X = []  # array_solucion

    # Recorrer cada comprador
    for i in range(0, numcompradores, 1):

        p = int(ofertas[i][0])
        c = int(ofertas[i][1])
        r = int(ofertas[i][2])
        accionactual = r

        # Crear cada posible accion en la matriz
        for j in range(r, c + 1, 1):
            beneficio = accionactual * p
            fila = [[j, beneficio, i + 1]]
            # filacaminos = [[j, beneficio, i + 1]]

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
    for i in range(0, numcolumnas + 1, 1):

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
                        if matriz[k][capacidadrestante] > mejoropcion:
                            # Si el elemento actual no es del mismo comprador
                            if matriz[k][0][2] != matriz[j][0][2]:
                                # Si el comprador no esta en el camino
                                if matriz[j][0][2] not in caminos[k][capacidadrestante]:
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

    return X, mejorpreciofinal
