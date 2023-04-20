def calcular_ofertas(entrada, combinacion_oferta):
    mejor_precio = 0
    ofertas = entrada[3]
    mejor_mensaje = ""
    n = entrada[2]
    accionesrestantes = entrada[0]
    precio = 0
    mensaje = ""
    mensaje_total = ""

    for j in combinacion_oferta:
        for i in range(0, n+1, 1):
            if(i != n):
                precio += int(ofertas[i][0])*int(j[i])
                accionesrestantes = accionesrestantes-j[i]
                mensaje += "Comprador " + \
                    str(i+1)+": " + \
                    str(j[i])+"($"+str(ofertas[i][0])+") | "
            else:
                mensaje += "Gov " + \
                    str(i+1)+": " + \
                    str(j[i])+"($"+str(ofertas[i][0])+") | "
                precio += int(ofertas[i][0])*int(j[i])
                accionesrestantes = accionesrestantes-j[i]
        mensaje_total += mensaje + str(precio) + "\n"
        if precio > mejor_precio:
            mejor_precio = precio
            mejor_mensaje = mensaje

        accionesrestantes = entrada[0]
        mensaje = ""
        precio = 0

    return [mensaje_total, "El mejor precio fue: " + str(mejor_precio)]


'''
Analiza las combinaciones con 0 y el maximo en cada posicion, creo que está correcto
Devuelve un array las combinaciones viables con 0 y el maximo en cada posicion
Si una convinacion no es viable, o sea, sea pasa de la cantidad de acciones a vender,
simplemente no se retorna 
Precondicion: las ofertas vienen ordenadas descendentemente por precio de accion
Funcion hallar combinaciones posibles 
A,B,n,ofertas @ [int,int,int,Array [ Array [] ] ] -> combinaciones_array @ [ Array [] ]
'''


def hallar_combinaciones(entrada):
    n = entrada[2]
    ofertas = entrada[3]
    combinaciones = []
    num_acciones_max = []

    for i in range(0, n):  # no se tiene en cuenta al gov
        num_acciones_max.append(int(ofertas[i][1]))

    combinacion_actual = []  # aqui se meten todas las combinaciones

    for i in num_acciones_max:
        combinacion_actual.append(0)

    # combinacion que no toma ninguna oferta privada
    combinaciones.append(combinacion_actual.copy()+[ofertas[n][1]])

    while True:
        for i in range(n-1, -1, -1):
            if (combinacion_actual[i] < num_acciones_max[i]):
                if combinacion_actual[i] == 0:
                    combinacion_actual[i] = num_acciones_max[i]

                    if (ofertas[n][1]-sum(combinacion_actual) >= 0):
                        combinaciones.append(combinacion_actual.copy(
                        )+[ofertas[n][1]-sum(combinacion_actual)])
                    break
            else:
                # verifica si ya se acabó
                fin = True
                for k in range(n-1, -1, -1):
                    if combinacion_actual[k] != num_acciones_max[k]:
                        fin = False
                if fin:
                    return combinaciones

                for k in range(n-1, i-1, -1):
                    combinacion_actual[k] = 0
    return combinaciones
