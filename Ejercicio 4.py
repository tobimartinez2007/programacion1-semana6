#Ejercicio 4

def ejercicio_a():
    lista = []
    for i in range (5):
        numero = int (input("Ingrese un número a la lista: "))
        lista.append(numero)

    tupla = tuple(lista)

    print (f"Primer elemento de la tupla: {tupla[0]}")
    print (f"Ultimo elemento de la tupla: {tupla[-1]}")

def ejercicio_b():
    lista = []
    rango = int(input("Ingresar el largo de la lista:"))
    for i in range (rango):
        numero = int (input("Ingrese un número a la lista: "))
        lista.append(numero)
    suma = 0
    for i in lista:
        suma = suma + i
    promedio = suma/rango

    tupla = tuple(lista)
    

    return tupla, promedio

def ejercicio_c():
    tupla = ("Rojo", "Amarillo", "Azul")
    lista = list(tupla)
    color_3 = lista.pop(-1)
    color_2 = lista.pop(1)
    color_1 = lista.pop(0)
    print (f"Color 1: {color_1}")
    print (f"Color 2: {color_2}")
    print (f"Color 3: {color_3}")

ejercicio_c()

tupla, promedio = ejercicio_b()

print (f"Promedio de las notas: {promedio}")
print (f"Tupla formada: {tupla}")






