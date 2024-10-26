Proceso MatemaicaDiscreta
    Definir n, r, resultado Como Entero
    Definir tipo, opcion Como Cadena
	
    Escribir "Ingrese el valor de n:"
    Leer n
    Escribir "Ingrese el valor de r:"
    Leer r
    Escribir "Ingrese el tipo (Sin repetición o Con repetición):"
    Leer tipo
    Escribir "Ingrese la opción (Permutaciones o Combinaciones):"
    Leer opcion
	
    Si n < 0 O r < 0 O (r > n Y tipo = "Sin repetición") Entonces
        Escribir "Error: Valores no válidos."
    Sino
        Si opcion = "Permutaciones" Entonces
            Si tipo = "Sin repetición" Entonces
                resultado = 1
                Para i = 0 Hasta r-1 Hacer
                    resultado = resultado * (n - i)
                FinPara
                Escribir "Permutaciones (Sin repetición): ", resultado
            Sino
                resultado = n ^ r
                Escribir "Permutaciones (Con repetición): ", resultado
            FinSi
        Sino
            Si tipo = "Sin repetición" Entonces
                resultado = 1
                Para i = 0 Hasta r-1 Hacer
                    resultado = resultado * (n - i)
                FinPara
                Para i = 1 Hasta r Hacer
                    resultado = resultado / i
                FinPara
                Escribir "Combinaciones (Sin repetición): ", resultado
            Sino
                resultado = 1
                Para i = 0 Hasta r-1 Hacer
                    resultado = resultado * (n + r - 1 - i)
                FinPara
                Para i = 1 Hasta r Hacer
                    resultado = resultado / i
                FinPara
                Escribir "Combinaciones (Con repetición): ", resultado
            FinSi
        FinSi
    FinSi
FinProceso
