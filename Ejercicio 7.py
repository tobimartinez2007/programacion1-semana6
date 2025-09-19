#Ejercicio 7:

print ("Inscripción a la asignatura Programación I")
numero_legajo = int(input("Ingresar el número de legajo del estudiante o 0 para finalizar: "))
lista_alumnos = []
print ("¡Muchas gracias!")
print ("")
while numero_legajo > 0:
    numero_legajo = int(input("Ingresar el número de legajo del estudiante o 0 para finalizar: "))
    lista_alumnos.append(numero_legajo)
    print ("¡Muchas gracias!")
    print ("")

print (f"La lista de inscriptos es: {lista_alumnos}")

