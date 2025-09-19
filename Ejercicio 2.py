# Ejercicio 2
def lista_max_min():
    lista = []
    for i in range (5):
        numero = int(input("Por favor, ingrese un número: "))
        lista.append(numero)
    print (f"Lista completa: {lista}")
    print (f"Numero mayor de la lista: {max(lista)}")
    print (f"Número menor de la lista: {min(lista)}")
    return lista

def lista_frutas():
    
    lista = ["pera", "banana", "manzana"]
    lista.append("uva")
    lista.pop(1) #también puede ser lista.remove("banana")
    print (lista)

def invertir_lista(l):
    nueva_lista = []
    while l != []:
        nuevo_elemento = l.pop(-1)
        nueva_lista.append(nuevo_elemento)
    return nueva_lista
    

#Código principal
lista_global = lista_max_min()
nueva_lista = invertir_lista(lista_global)
print (f"La nueva lista es: {nueva_lista}")