using System;

class Program
{    static void Main()
    {
        // 1. Inicialización
        int contador = 1;
        // 2. Condición: Mientras el contador sea menor o igual a 5
        while (contador <= 5)
        {
            Console.WriteLine($"Número: {contador}");
            // 3. Actualización (Vital para evitar el bucle infinito)
            contador++; 
        }
        Console.WriteLine("¡Bucle terminado!");
    }
}