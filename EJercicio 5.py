#EJercicio 5

def últimos_caracteres():
    cadena = input("Por favor, ingrese una cadena: ")
    cadena = cadena[::-1]
    ultimos = cadena[0:3]
    ultimos =  ultimos [::-1]
    print (ultimos)



def contar(c, s):
    contador = 0
    for i in s:
        if i == c:
            contador = contador +1
    
    return contador

def contar_vocales (s):
    s = s.lower()  # Ignorar mayúsculas/minúsculas
    vocales = "aeiou"  # Lista de vocales
    for v in vocales:
        contador = 0
        for letra in s:
            if letra == v:
                contador += 1
        print(f"Cantidad de veces que aparece <<{v}>>: {contador}")


cadena = input("Ingresar una cadena: ")
caracter = input ("Ingresar un caracter: ")
contador = contar(caracter, cadena)
print (f"Cantidad de veces que aparece el caracter en la cadena: {contador}")
contar_vocales(cadena)



