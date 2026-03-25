#Entrada de datos
edad =int(input("Ingrese su edad "))
promedio =float(input("Ingrese su promedio "))

#Primer If
if edad>=18:
    print ("Cumples la edad minima")
    #Segungo IF
    if promedio>=16:
        print("candidato apto para beca18")
    else:
        print("promedio insuficiente")
else:
    print("Debe ser mayor de 18 años")            