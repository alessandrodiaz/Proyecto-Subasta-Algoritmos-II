from IO import leer_entrada, escribir_salida
from accionesFB import accionesFB
from accionesV import accionesV
from accionesPD1 import accionesPD1
from accionesPD2 import accionesPD2


archivo = None
archivo_salida = "salida.txt"

if __name__ == '__main__':

    nombre_programa = "SUBASTA PUBLICA DE ACCIONES"
    nombre_programa_centrado = nombre_programa.center(20, ' ')
    print(nombre_programa_centrado)
    print("¿Que archivos deseas elegir?")
    archivo = input('Escribe el nombre del archivo: ')
    print("¿Con que algoritmo te gustaria resolver el problema?")
    print("\t 1. Fuerza bruta")
    print("\t 2. Algoritmo voraz")
    print("\t 3. Programación dinámica")
    print("\t 4. Programación dinámica con paquetes de acciones")

    print("-----------------------------------------------------------------")
 
    A, B, n, ofertas, tamano_paquetes = leer_entrada(archivo)
    # print(A,B,n,ofertas)
    eleccion = None
    resultado = None

    while eleccion != '1' and eleccion != '2' and eleccion != '3' and eleccion != '4':
        eleccion = input('Elije que algoritmo quieres usar: ')
        print("El algoritmo que elejiste fue: ", eleccion)
        print("El archivo entrada que elejiste fue: ", archivo)
        if eleccion == '1':
            resultado = accionesFB(A, B, n, ofertas)
            print(resultado)
            escribir_salida(resultado, archivo_salida)
        elif eleccion == '2':
            resultado = accionesV(A, B, n, ofertas)
            print(resultado)
            escribir_salida(resultado, archivo_salida)
        elif eleccion == "3" and archivo.endswith('.sub'):
            resultado = accionesPD1(A, B, n, ofertas)
            print(resultado)
            escribir_salida(resultado, archivo_salida)
        elif eleccion == "4" and tamano_paquetes != None and archivo.endswith('.psub'):
            resultado = accionesPD2(A, B, n, ofertas, tamano_paquetes)
            print(resultado)
            escribir_salida(resultado, archivo_salida)
        else:
            print("Por favor elije una opcion valida\n")

print("Tu salida ya se encuentra en el archivo salida.txt")


