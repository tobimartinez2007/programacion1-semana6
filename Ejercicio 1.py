#Ejercicio 1 


def transformar_palabra(p):
    """
    Recibe una cadena y la transforma a todo mayúscula, todo minúscula y formato titulo.

    """
    
    palabra_minuscula = p.lower()
    palabra_mayuscula = p.upper()
    palabra_titulo = p.title()

    print (f"Palabra ingresada: {p} ")
    print (f"Palabra convertida a minuscula: {palabra_minuscula} ")
    print (f"Palabra convertida a mayúscula: {palabra_mayuscula} ")
    print (f"Palabra con mayúscula en la primera letra: {palabra_titulo} ")


def contar_frase(f):
    """
    Recible una frase, divide cada palabra en elementos de una lista y cuenta la cantida de elementos
    de la misma
    """
    
    palabras = f.split()
    print(f"Cantidad de palabras de la frase: {len(palabras)}")


def reemplazar_vocales (p):
    """
    Recibe una cadea e itera sobre la misma. Si una de las letras es una vocal, la reemplaza
    con un "*"
    """

    vocales = "aeiouAEIOU"
    nueva_palabra = ""
    for letra in p:
        if letra in vocales:
            nueva_palabra = nueva_palabra + "*"
        else:
            nueva_palabra = nueva_palabra + letra
    print (f"Palabra formada: {nueva_palabra}")


def menu():
    """
    Muestra las opciones disponibles y devuelve la opción elegida.
    """


    print ("Opciones disponibles:")
    print ("1. Transformar palabra")
    print ("2. Contar palabras de una frase")
    print ("3. Reemplazar vocales de una palabra")
    print ("4. Salir")
    opcion = int(input("Por favor, ingrese una opción:"))
    return opcion


#Código Principal: 


opcion = menu()
while opcion != 4:
    match opcion:
        case 1:
            palabra = input("Por favor, ingrese una palabra: ")
            transformar_palabra(palabra)
            opcion = menu()
            
        case 2: 
            frase = input("Por favor, ingrese una frase: ")
            contar_frase(frase)
            opcion = menu()

        case 3: 
            palabra = input("Por favor, ingrese una palabra:")
            reemplazar_vocales (palabra)
            opcion = menu()

        case _:
            opcion = input("Error, ingrese una opción válida: ")


print ("¡Gracias! vuelva pronto.")


