# Inicialización
contador = 1

# Condición: Mientras el contador sea menor o igual a 5
while contador <= 5:
    print(f"Número: {contador}")
    
    # Actualización (Crucial para evitar bucles infinitos)
    contador += 1 

print("¡Bucle terminado!")