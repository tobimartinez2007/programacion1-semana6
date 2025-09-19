#Ejercicio 3


def matriz_2x2():
    # Crear matriz vacía
    matriz = []

    # Pedir números al usuario
    for i in range(2):          # filas
        fila = []
        for j in range(2):      # columnas
            numero = int(input(f"Ingrese el número para la posición [{i}][{j}]: "))
            fila.append(numero)
        matriz.append(fila)

    # Mostrar la matriz como tabla
    print("\nMatriz 2x2:")
    for fila in matriz:
        print(fila)

def matriz_3x3():
    matriz = []
    for i in range (3):
        fila = []
        for j in range (3):
            numero = int(input(f"Ingrese el número para la posición [{i}][{j}]: "))
            fila.append(numero)
        matriz.append(fila)
    
    suma = 0
    for fila in matriz:
        for numero in fila:
            suma = suma + numero
    
    print (f"Suma de los elemetnos de la matriz: {suma}")

matriz_3x3()