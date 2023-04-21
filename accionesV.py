'''
Toma primero la mayor cantidad de acciones que el primer
comprador puede comprar, luego toma la mayor cantidad el
segundo comprador puede comprar... asi hasta asignar
las acciones restantes al gobierno.
Funcion accionesV
A,B,n,ofertas @ [str,str,str,Array [ Array [] ] ] -> pareja @ [ Array [], int ]
'''


def accionesV(A, B, n, ofertas):
    accionesrestantes = int(A)
    precio = 0
    X = []  # array_solucion

    # Ofertas vienen ordenadas de mayor a menor precio por accion
    for i in range(0, n, 1):
        max_acciones = int(ofertas[i][1])
        min_acciones = int(ofertas[i][2])
        precio_accion = int(ofertas[i][0])

        if max_acciones <= accionesrestantes:
            accionesrestantes = accionesrestantes - max_acciones
            precio += max_acciones * precio_accion
            X.append(max_acciones)

        elif min_acciones <= accionesrestantes:
            precio += accionesrestantes * precio_accion
            X.append(accionesrestantes)
            accionesrestantes = 0
        else:
            X.append(0)

    return (X, precio)
