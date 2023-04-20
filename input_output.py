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


def leer_entrada(filename):

    A = None  # Numero total de acciones a la venta
    B = None  # Precio mínimo por acción
    n = None  # Número de ofertas de compradores

    ofertas = []

    with open(filename, "r") as archivo:
        lineas = archivo.readlines()
        A = int(lineas[0])
        B = int(lineas[1])
        n = int(lineas[2])

        for linea in lineas[3:]:
            oferta = linea.strip().split(",")

            p = int(oferta[0])  # Precio por acción
            c = int(oferta[1])  # Máximo de acciones que compraría
            r = int(oferta[2])  # Mínimo de acciones que compraría

            ofertas.append([p, c, r])

    return A, B, n, ofertas


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


def escribir_salida(texto):
    pass
