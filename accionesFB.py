'''
Analiza las combinaciones con 0 y el maximo en cada posicion, creo que está correcto
Devuelve un array las combinaciones viables con 0 y el maximo en cada posicion
Si una convinacion no es viable, o sea, sea pasa de la cantidad de acciones a vender,
simplemente no se retorna 
Precondicion: las ofertas vienen ordenadas descendentemente por precio de accion
Funcion hallar_combinaciones_posibles 
A,B,n,ofertas @ [str,str,str,Array [ Array [] ] ] -> combinaciones_array @ [ Array [] ]
'''


def hallar_combinaciones_posibles(A, B, n, ofertas):
    combinaciones = []
    num_acciones_max = []

    for i in range(0, n-1):  # no se tiene en cuenta al gov
        num_acciones_max.append(int(ofertas[i][1]))

    combinacion_actual = []  # aqui se meten todas las combinaciones

    for i in num_acciones_max:
        combinacion_actual.append(0)

    # combinacion que no toma ninguna oferta privada
    combinaciones.append(combinacion_actual.copy()+[ofertas[n-1][1]])

    while True:
        for i in range(n-2, -1, -1):
            if (combinacion_actual[i] < num_acciones_max[i]):
                if combinacion_actual[i] == 0:
                    combinacion_actual[i] = num_acciones_max[i]

                    if (ofertas[n-1][1]-sum(combinacion_actual) >= 0):
                        combinaciones.append(combinacion_actual.copy(
                        )+[ofertas[n-1][1]-sum(combinacion_actual)])
                    break
            else:
                # verifica si ya se acabó
                fin = True
                for k in range(n-2, -1, -1):
                    if combinacion_actual[k] != num_acciones_max[k]:
                        fin = False
                if fin:
                    return combinaciones

                for k in range(n-2, i-1, -1):
                    combinacion_actual[k] = 0
    return combinaciones


'''
devuelve una pareja: un array X en donde se encuentra la compra de
cada comprador y del gobierno y el otro elemento...
Funcion accionesFB
A,B,n,ofertas @ [str,str,str,Array [ Array [] ] ] -> pareja @ [ Array [], int ]
'''


def accionesFB(A, B, n, ofertas):
    combinaciones_posibles = hallar_combinaciones_posibles(A, B, n, ofertas)

    mejor_precio = 0
    precio = 0

    X = []  # arrary solucion
    X_aux = []  # array con solucion temporal

    for paquete in combinaciones_posibles:
        for i in range(0, n, 1):
            precio += int(ofertas[i][0])*int(paquete[i])
            X_aux.append(paquete[i])
        if precio > mejor_precio:
            mejor_precio = precio
            X = X_aux.copy()
        X_aux.clear()
        precio = 0

    return (X, mejor_precio)
