
def accionesPD2(A, B, n, ofertas, tamano_paquetes):

    # Ir guardando la mejor solucion y los compradores incluidos
    solucionvalor = 0
    solucioncaminos = None

    A = int(A)
    # Crear diccionario de beneficios por columnas:idcomprador:peso
    matriz = {}
    # Diccionario de caminos (compradores incluidos en una oferta)
    # columnas:idcomprador:idcompradores:numero de acciones
    caminos = {}
    numcompradores = n

    # Analogia con problema de la mochila
    # "Peso" = numero de acciones de un comprador
    # "Beneficio" = dinero
    # "Capacidad" = Numero de acciones que tiene la subasta en el momento

    # Recorrer cada accion
    i = tamano_paquetes

    # Termina hasta que se haya leído la matriz y haya regresado hasta los valores de r de todos los compradores
    continuar = True
    while continuar:
        # print(i)
        # Craer nueva "columna" (accion)
        matriz[i] = {}
        caminos[i] = {}

        # Recorrer cada comprador
        for j in range(0, numcompradores, 1):

            p = int(ofertas[j][0])
            c = int(ofertas[j][1])
            r = int(ofertas[j][2])
            idcomprador = j+1
            caminos[i][idcomprador] = {}

            if i <= A:
                # Si estamos en el rango de acciones que un comprador esta dispuesto a dar
                if r <= i <= c:
                    # Simplemente agregamos la nueva oferta
                    matriz[i][idcomprador] = i*p
                    caminos[i][idcomprador][idcomprador] = i

                    # Revisamos si esta es la mejor solucion de momento
                    if matriz[i][idcomprador] > solucionvalor:
                        solucionvalor = matriz[i][idcomprador]
                        solucioncaminos = caminos[i][idcomprador]

                # Si la capacidad que se esta leyendo es mayor a "c" lo que esta dispuesto a dar un comprador
                elif i > c:
                    # Capacidad que se esta leyendo actualmente menos el maximo que esta dispuesto un comprador a dar
                    capacidadrestante = i-c
                    max_columna = 0.0
                    nuevoscompradores = {}

                    # Revisamos en la capacidad restante la mejor oferta para completar las A acciones
                    # El comprador no puede estar en esa oferta (ya que estaria 2 veces en una oferta)
                    for key_comp_externo, beneficio in matriz[capacidadrestante].items():
                        if key_comp_externo != idcomprador and beneficio > max_columna and idcomprador not in caminos[capacidadrestante][key_comp_externo]:
                            max_columna = beneficio
                            # Tomamos los compradores de esa mejor oferta
                            nuevoscompradores = caminos[capacidadrestante][key_comp_externo]

                    # Si existe una oferta que puede completar las A acciones
                    # Creamos una nueva oferta con el comprador y el comprador o compradores externos
                    if max_columna > 0:
                        caminos[i][idcomprador][idcomprador] = c
                        caminos[i][idcomprador].update(nuevoscompradores)
                        matriz[i][idcomprador] = max_columna+c*p
                    # Si no la mejor oferta es que el comprador de el maximo que esta dispuesto a dar
                    else:
                        caminos[i][idcomprador][idcomprador] = c
                        matriz[i][idcomprador] = c*p

                    # Revisamos si esta es la mejor solucion de momento
                    if matriz[i][idcomprador] > solucionvalor:
                        solucionvalor = matriz[i][idcomprador]
                        solucioncaminos = caminos[i][idcomprador]

            # Si ya leimos toda la capacidad (A) de la subasta tomando el maximo (c) de cada comprador
            # Ahora nos devolvemos leyendo las posibles ofertas con valores menores a (c) y minimo (r) de cada comprador
            else:
                accion_revisar = i-A
                accion_revisar = c-accion_revisar

                # Si no hemos terminado de leer todas las acciones del comprador
                if accion_revisar >= r:
                    # Mismo procedimiento pero con numero de acciones distintos al maximo de cada comprador
                    capacidadrestante = A-accion_revisar
                    max_columna = 0.0
                    nuevoscompradores = {}

                    for key_comp_externo, beneficio in matriz[capacidadrestante].items():
                        if key_comp_externo != idcomprador and beneficio > max_columna and idcomprador not in caminos[capacidadrestante][key_comp_externo]:
                            max_columna = beneficio
                            nuevoscompradores = caminos[capacidadrestante][key_comp_externo]

                    if max_columna > 0:
                        caminos[i][idcomprador][idcomprador] = accion_revisar
                        caminos[i][idcomprador].update(nuevoscompradores)
                        matriz[i][idcomprador] = max_columna+accion_revisar*p
                    else:
                        caminos[i][idcomprador][idcomprador] = accion_revisar
                        matriz[i][idcomprador] = accion_revisar*p

                    # Revisamos si esta es la mejor solucion de momento
                    if matriz[i][idcomprador] > solucionvalor:
                        solucionvalor = matriz[i][idcomprador]
                        solucioncaminos = caminos[i][idcomprador]
                # Si soy el ultimo comprador y ya se leyeron todas las acciones, terminamos
                elif (j+1) == numcompradores:
                    continuar = False

        i += tamano_paquetes

    # Impresion
    # for key, value in matriz.items():
    #     print(key, ' : ', value)
    # print("CAMINOS")
    # for key, value in caminos.items():
    #     print(key, ' : ', value)

    arraysolucion = []

    for i in range(1, numcompradores, 1):
        if i in solucioncaminos:
            arraysolucion.append(solucioncaminos[i])
        else:
            arraysolucion.append(0)

    return arraysolucion, solucionvalor
