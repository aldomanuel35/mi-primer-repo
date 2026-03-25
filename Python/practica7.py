contador = 1

while True:
    print(f"El contador vale: {contador}")
    contador += 1
    
    # Aquí es donde "pensamos" si debemos seguir o no (al final)
    if contador > 3:
        break # Esto detiene el bucle

print("¡Fin de la simulación!")