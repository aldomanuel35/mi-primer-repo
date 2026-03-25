opcion = int(input("Seleciona un color (1-3):"))

match opcion:
    case 1:
        print ("Elegiste color Rojo")
    case 2:
        print ("Elegiste color Azul")
    case 3:
        print ("Elegiste color Verde")
    case _: 
        print ("Elegiste opción no valida")