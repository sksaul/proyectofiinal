Proceso MatemaicaDiscreta
    Definir n, r, resultado Como Entero
    Definir tipo, opcion Como Cadena
	
    Escribir "Ingrese el valor de n:"
    Leer n
    Escribir "Ingrese el valor de r:"
    Leer r
    Escribir "Ingrese el tipo (Sin repetici�n o Con repetici�n):"
    Leer tipo
    Escribir "Ingrese la opci�n (Permutaciones o Combinaciones):"
    Leer opcion
	
    Si n < 0 O r < 0 O (r > n Y tipo = "Sin repetici�n") Entonces
        Escribir "Error: Valores no v�lidos."
    Sino
        Si opcion = "Permutaciones" Entonces
            Si tipo = "Sin repetici�n" Entonces
                resultado = 1
                Para i = 0 Hasta r-1 Hacer
                    resultado = resultado * (n - i)
                FinPara
                Escribir "Permutaciones (Sin repetici�n): ", resultado
            Sino
                resultado = n ^ r
                Escribir "Permutaciones (Con repetici�n): ", resultado
            FinSi
        Sino
            Si tipo = "Sin repetici�n" Entonces
                resultado = 1
                Para i = 0 Hasta r-1 Hacer
                    resultado = resultado * (n - i)
                FinPara
                Para i = 1 Hasta r Hacer
                    resultado = resultado / i
                FinPara
                Escribir "Combinaciones (Sin repetici�n): ", resultado
            Sino
                resultado = 1
                Para i = 0 Hasta r-1 Hacer
                    resultado = resultado * (n + r - 1 - i)
                FinPara
                Para i = 1 Hasta r Hacer
                    resultado = resultado / i
                FinPara
                Escribir "Combinaciones (Con repetici�n): ", resultado
            FinSi
        FinSi
    FinSi
FinProceso
