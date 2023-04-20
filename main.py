from input_output import leer_entrada, escribir_salida
from fuerza_bruta import hallar_combinaciones, calcular_ofertas
from voraz import voraz
from programacion_dinamica import programacion_dinamica

nombre_de_archivo = "entrada.txt"

if __name__ == '__main__':
    print("---------FUERZA BRUTA---------", "\n")
    entrada = leer_entrada(nombre_de_archivo)
    combinaciones = hallar_combinaciones(entrada)
    mensaje, mejor_precio = calcular_ofertas(entrada, combinaciones)
    print(entrada, "\n")
    print(mensaje)
    print(mejor_precio, "\n")

    print("---------VORAZ---------")
    voraz(entrada)
    print("\n")

    print("---------PROGRAMACION DINAMICA---------")
    programacion_dinamica(entrada)
