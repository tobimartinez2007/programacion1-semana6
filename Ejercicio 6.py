#Ejercicio 6:

def contar_palabras (c):
    contador_letras = 0
    contador_palabras = 0

    lista_palabras = c.split()
    for palabra in lista_palabras:
        if len(palabra) > 4:
            contador_palabras += 1
    return contador_palabras
                

    
cadena = input("Ingresar una frase: ")
resultado = contar_palabras(cadena)
print (f"Cantidad de palabras con más de 4 letras en la frase: {resultado}")
