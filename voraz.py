def voraz(entrada):
    print(entrada)
    A = entrada[0]
    B = entrada[1]
    n = entrada[2]
    ofertas = entrada[3]
    p_gov = entrada[3][n][0]

    accionesrestantes = int(A)
    precio = 0

    # Ofertas vienen ordenadas de mayor a menor precio por accion
    for i in range(0, n, 1):
        max_acciones = int(ofertas[i][1])
        min_acciones = int(ofertas[i][2])
        precio_accion = int(ofertas[i][0])

        if max_acciones <= accionesrestantes:
            accionesrestantes = accionesrestantes - max_acciones
            precio += max_acciones * precio_accion
            print("Comprador " + str(i + 1) + ": " + str(max_acciones) + " $" +
                  str(precio_accion))

        elif min_acciones <= accionesrestantes:
            precio += accionesrestantes * precio_accion
            print("Comprador " + str(i + 1) + ": " + str(accionesrestantes) + " $" +
                  str(precio_accion))
            accionesrestantes = 0

        else:
            print("Comprador " + str(i + 1) + ": No puede comprar")

    if accionesrestantes > 0:
        precio += int(p_gov) * accionesrestantes
    print("Gobierno: " + str(accionesrestantes) + " $" + str(p_gov))
    print("TOTAL: " + str(precio))
