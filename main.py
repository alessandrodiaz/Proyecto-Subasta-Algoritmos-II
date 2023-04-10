'''
Las salidas se deben producir en un archivo de texto con n + 2 líneas así:
Costo
x1
x2
.
.
.
xn
resto
Es decir, la primera línea trae el costo de la solución, y las siguientes n líneas las acciones asignadas a cada oferente y la última línea el resto de acciones que son las asignadas al gobierno.
'''


'''
Las entradas vendrían en un archivo de texto con n + 4 líneas así:
A
B
n
p1,c1,r1
p2,c2,r2
.
.
.
pn,cn,rn
B,A,0
Es decir, la primera línea trae el número de acciones (un entero), la segunda el precio mínimo por acción (un entero), la tercera el número de compradores (un entero), las siguientes n líneas los tres enteros separados por comas, que representan las ofertas de cada comprador, y la última línea con la oferta del gobierno.
'''

'''
Funcion leer archivo
file.txt -> [A,B,n,ofertas] @ [int,int,int,Array [ Array [] ] ]
'''

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

with open("entrada.txt", "r") as archivo:
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


'''
Precondicion: las ofertas vienen ordenadas descendentemente por precio de accion
Funcion hallar combinaciones posibles
A,B,n,ofertas @ [int,int,int,Array [ Array [] ] ] -> combinaciones_array @ Array [int]
'''

'''
Funcion hallar solucion
combinaciones_array @ Array [int] -> solucion @ Array [int]
'''


print("/////////////////////////////////////////////////////")

'''
Analiza absolutamente todas las combinaciones, creo que está correcto
'''


def combinaciones_v4(arr, n):
    num_acciones_min = []
    num_acciones_max = []
    for i in range(0, n):  # no se tiene en cuenta al gov
        num_acciones_max.append(int(arr[i][1]))
        num_acciones_min.append(int(arr[i][2]))
    print("/////////////////////////////////////////////////////")
    arr_aux = []  # aqui se meten todas las combinaciones vistas en pantalla

    for i in num_acciones_min:
        arr_aux.append(0)
    print(arr_aux)  # linea que no toma ninguna oferta privada
    while True:
        for i in range(n-1, -1, -1):
            if (arr_aux[i] + 1 <= num_acciones_max[i]):
                if arr_aux[i] == 0:
                    arr_aux[i] = num_acciones_min[i]
                    print(arr_aux)
                    break
                else:
                    arr_aux[i] = arr_aux[i] + 1
                print(arr_aux)
                break
            else:
                fin = True
                for k in range(n-1, -1, -1):
                    if arr_aux[k] != num_acciones_max[k]:
                        fin = False
                if fin:
                    return arr_aux

                for k in range(n-1, i-1, -1):
                    arr_aux[k] = 0

# combinaciones_v4(ofertas,int(n))


"""

"""


def calcular_oferta(combinacion_oferta):
    global mejor_precio, mejor_mensaje
    accionesrestantes = int(A)
    precio = 0
    mensaje = ""

    for i in range(0, int(n), 1):
        if(accionesrestantes >= combinacion_oferta[i]):
            precio += int(ofertas[i][0])*int(combinacion_oferta[i])
            accionesrestantes = accionesrestantes-combinacion_oferta[i]
            mensaje += "Comprador " + \
                str(i+1)+": " + \
                str(combinacion_oferta[i])+"($"+ofertas[i][0]+") | "
        else:
            mensaje += "Comprador " + str(i+1)+": NO | "

    if accionesrestantes > 0:
        precio += int(p_gov)*accionesrestantes

    mensaje += "Gobierno: " + str(accionesrestantes)

    print(mensaje, precio)

    if precio > mejor_precio:
        mejor_precio = precio
        mejor_mensaje = mensaje


'''
Analiza las combinaciones con 0 y el maximo en cada posicion, creo que está correcto
'''


def combinaciones_v5(arr, n):
    # num_acciones_min = []
    num_acciones_max = []

    for i in range(0, n):  # no se tiene en cuenta al gov
        num_acciones_max.append(int(arr[i][1]))
        # num_acciones_min.append(int(arr[i][2]))
    print("/////////////////////////////////////////////////////", A, B, n)

    arr_aux = []  # aqui se meten todas las combinaciones vistas en pantalla

    for i in num_acciones_max:
        arr_aux.append(0)
    print(arr_aux)  # linea que no toma ninguna oferta privada
    calcular_oferta(arr_aux)

    while True:
        for i in range(n-1, -1, -1):
            if (arr_aux[i] < num_acciones_max[i]):
                if arr_aux[i] == 0:
                    arr_aux[i] = num_acciones_max[i]
                    calcular_oferta(arr_aux)

                    print(arr_aux)
                    break
            # cuando en i no se pueden aumentar las acciones, se resetean desde n-1 a i-1
            # (hasta i por el for) a 0 y se sigue con el siguiente i
            else:

                # cada vez que un i llegue al maximo de acciones, revisar si las demas tambien lo estan
                fin = True
                for k in range(n-1, -1, -1):
                    if arr_aux[k] != num_acciones_max[k]:
                        fin = False
                if fin:
                    return arr_aux

                for k in range(n-1, i-1, -1):
                    arr_aux[k] = 0


# combinaciones_v5(ofertas, int(n))

# print("MEJOR OFERTA: $", mejor_precio, " - ", mejor_mensaje)


'''
POR HACER:
  restar a cada arr_aux mostrado en pantalla, las acciones del gov. Y sumarlas en un arr_final en una posicion adicional al final
  con todos los arr_final, hallar el valor de cada combinacion de ofertas, y elegir el mayor.
'''


def voraz(ofertas, n):
    accionesrestantes = int(A)
    precio = 0

    # Ofertas vienen ordenadas de mayor a menor precio por accion
    for i in range(0, n, 1):
        max_acciones = int(ofertas[i][1])
        min_acciones = int(ofertas[i][2])
        precio_accion = int(ofertas[i][0])

        if max_acciones <= accionesrestantes:
            accionesrestantes = accionesrestantes-max_acciones
            precio += max_acciones*precio_accion
            print("Comprador "+str(i+1)+": " +
                  str(max_acciones)+" $"+str(precio_accion))

        elif min_acciones <= accionesrestantes:
            precio += accionesrestantes*precio_accion
            print("Comprador "+str(i+1)+": " +
                  str(accionesrestantes)+" $"+str(precio_accion))
            accionesrestantes = accionesrestantes-accionesrestantes

        else:
            print("Comprador "+str(i+1)+": No puede comprar")

    if accionesrestantes > 0:
        precio += int(p_gov)*accionesrestantes
    print("Gobierno: "+str(accionesrestantes)+" $"+str(p_gov))
    print("TOTAL: "+str(precio))


# voraz(ofertas, int(n))


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
                        caminos[j][i] = compradores
                        caminos[j][i].append(comprador)

    def imprimir_matriz(matriz):
        for fila in matriz:
            for celda in fila:
                print("{:<6}".format(str(celda)), end="")
            print()
    # imprimir_matriz(matriz)
    print("--> MATRIZ CAMINOS")

    def imprimir_matriz(matriz):
        for fila in matriz:
            for celda in fila:
                print("{:<10}".format(str(celda)), end="")
            print()
    # imprimir_matriz(caminos)


programacion_dinamica(ofertas, int(n))
