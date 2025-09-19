#Ejercicio 8

def matriz_3x3():

    #Ingresar matriz
    numero_filas = int(input("Ingrese el número de filas de la matriz: "))
    numero_columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matriz = []
    for i in range (numero_filas):
        fila = []
        for j in range (numero_columnas):
            numero = int(input(f"Ingrese el número para la posición [{i}][{j}]: "))
            fila.append(numero)
        matriz.append(fila)
    
    # Mostrar la matriz como tabla
    print("\nMatriz 2x2:")
    for fila in matriz:
        print(fila)

    suma = 0
    for fila in matriz:
        for numero in fila:
            suma = suma + numero
    
    print (f"Suma de los elemetnos de la matriz: {suma}")

matriz_3x3()