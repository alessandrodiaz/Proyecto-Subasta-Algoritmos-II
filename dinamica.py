# Numero total de acciones a la venta
import copy
A = None
# Precio mínimo por acción
B = None
# Número de ofertas de compradores
n = None
# Precio por acción gobierno
p_gov = None

mejor_precio = 0
mejor_mensaje = ""

ofertas = []

with open("entrada2.txt", "r") as archivo:
    lineas = archivo.readlines()
    A = lineas[0]
    B = lineas[1]
    n = lineas[2]
    print(A, B, n)

    for linea in lineas[3:]:
        oferta = linea.strip().split(",")

        # Precio por acción
        p = oferta[0]
        # Máximo de acciones que compraría
        c = oferta[1]
        # Mínimo de acciones que compraría
        r = oferta[2]

        # Guarda el último precio por acción (gobierno)
        p_gov = oferta[0]

        ofertas.append([p, c, r])


print(ofertas)


def programacion_dinamica(ofertas, n):

    # A = entrada[0]

    # B = entrada[1]
    # n = entrada[2]
    # ofertas = entrada[3]
    # p_gov = entrada[3][n][0]

    matriz = []
    caminos = []
    numcompradores = n + 1

    for i in range(0, numcompradores, 1):  # Recorrer cada comprador

        p = int(ofertas[i][0])
        c = int(ofertas[i][1]) + 1
        r = int(ofertas[i][2])
        accionactual = r

        for j in range(r, c, 1):  # Crear cada posible accion en la matriz
            beneficio = accionactual * p
            fila = [[j, beneficio, i + 1]]
            filacaminos = [[j, beneficio, i + 1]]

            matriz.append(fila)
            caminos.append(filacaminos)
            accionactual += 1

    # Llenar datos de la matriz
    numcolumnas = int(A) + 1

    for i in range(0, numcolumnas, 1):

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

            # Empezamos a hacer calculos desde la accion 2
            if i > 1:
                comprador = 0
                compradores = []
                mejorescompradores = []
                columna = i
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

                                    # Tomamos comprador actual
                                    comprador = copy.copy(matriz[j][0][2])

                                    compradores = copy.copy(
                                        caminos[k][capacidadrestante])

                    if mejoropcion > 0:

                        matriz[j][i] = mejoropcion + matriz[j][0][1]

                        # print(comprador)

                        compradores.insert(0, comprador)

                        caminos[j][i] = compradores
                        caminos[j][i].insert(
                            int(len(caminos[j][i])/2)+1, [matriz[j][0][0]])

                        # caminos[j][i].append([matriz[j][0][0]])

    def imprimir_matriz(matriz):
        for fila in matriz:
            for celda in fila:
                print("{:<6}".format(str(celda)), end="")
            print()
    # imprimir_matriz(matriz)
    print("--> MATRIZ CAMINOS")

    # def imprimir_matriz(matriz):
    #     for fila in matriz:
    #         for celda in fila:
    #             print("{:<18}".format(str(celda)), end="")
    #         print()
    # imprimir_matriz(caminos)

    # for i in range(len(caminos)):
    # print(caminos[i])

    mejoropcion = 0
    respuesta = ""
    for i in range(0, len(matriz), 1):

        if matriz[i][int(A)] > mejoropcion:
            mejoropcion = matriz[i][int(A)]
            respuesta = caminos[i][int(A)]

    mensaje = ""
    numcompradores = int(len(respuesta)/2)
    iterar = numcompradores
    for i in range(0, numcompradores, 1):
        mensaje += "Comprador " + \
            str(respuesta[i])+": "+str(respuesta[iterar])+" | "
        iterar += 1

    print("\n---> COMPRADORES:", mensaje, "\n---> PRECIO MAXIMO:", mejoropcion)


programacion_dinamica(ofertas, int(n))
