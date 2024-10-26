Algoritmo algebra
	Definir opcion Como Entero
	Escribir 'Seleccione una opción:'
	Escribir '1. Inversa de una Matriz'
	Escribir '2. Multiplicar dos Matrices'
	Leer opcion
	Según opcion Hacer
		1:
			InversaMatriz()
		2:
			MultiplicarMatrices()
		De Otro Modo:
			Escribir 'Opción no válida.'
	FinSegún
FinAlgoritmo

Función InversaMatriz
	Definir a, b, c, d, det Como Real
	Escribir 'Ingrese los elementos de la matriz 2x2:'
	Escribir 'a:'
	Leer a
	Escribir 'b:'
	Leer b
	Escribir 'c:'
	Leer c
	Escribir 'd:'
	Leer d
	// Calcular el determinante
	det <- a*d-b*c
	Si det=0 Entonces
		Escribir 'La matriz no tiene inversa.'
	SiNo
		Escribir 'La inversa de la matriz es:'
		Escribir d/det, ' ', -b/det
		Escribir -c/det, ' ', a/det
	FinSi
FinFunción

Función MultiplicarMatrices
	Definir a1, b1, c1, d1, a2, b2, c2, d2 Como Real
	Definir r1, r2, r3, r4 Como Real
	Escribir 'Ingrese los elementos de la primera matriz 2x2:'
	Escribir 'a1:'
	Leer a1
	Escribir 'b1:'
	Leer b1
	Escribir 'c1:'
	Leer c1
	Escribir 'd1:'
	Leer d1
	Escribir 'Ingrese los elementos de la segunda matriz 2x2:'
	Escribir 'a2:'
	Leer a2
	Escribir 'b2:'
	Leer b2
	Escribir 'c2:'
	Leer c2
	Escribir 'd2:'
	Leer d2
	// Realizar la multiplicación
	r1 <- a1*a2+b1*c2
	r2 <- a1*b2+b1*d2
	r3 <- c1*a2+d1*c2
	r4 <- c1*b2+d1*d2
	Escribir 'El resultado de la multiplicación es:'
	Escribir r1, ' ', r2
	Escribir r3, ' ', r4
FinFunción

Funcion SinTitulo
	
FinFuncion
