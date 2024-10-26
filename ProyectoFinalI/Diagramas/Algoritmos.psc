Algoritmo Algoritmos 
	Definir opcion, total_productos, total_clientes, total_ventas Como Entero
	Definir productos, clientes, ventas Como Cadena
	total_productos <- 0
	total_clientes <- 0
	total_ventas <- 0
	Mientras opcion<>7 Hacer
		Escribir 'Menú Principal'
		Escribir '1. Agregar Producto'
		Escribir '2. Listar Productos'
		Escribir '3. Agregar Cliente'
		Escribir '4. Listar Clientes'
		Escribir '5. Registrar Venta'
		Escribir '6. Listar Ventas'
		Escribir '7. Salir'
		Leer opcion
		Según opcion Hacer
			1:
				Si total_productos<100 Entonces
					Escribir 'Ingrese el nombre del producto: '
					Leer productos
					total_productos <- total_productos+1
					Escribir 'Producto agregado.'
				FinSi
			2:
				Si total_productos=0 Entonces
					Escribir 'No hay productos registrados.'
				SiNo
					Para i<-0 Hasta total_productos-1 Hacer
						Escribir 'Producto ', i+1, ': ', productos
					FinPara
				FinSi
			3:
				Si total_clientes<100 Entonces
					Escribir 'Ingrese el nombre del cliente: '
					Leer clientes
					total_clientes <- total_clientes+1
					Escribir 'Cliente agregado.'
				FinSi
			4:
				Si total_clientes=0 Entonces
					Escribir 'No hay clientes registrados.'
				SiNo
					Para i<-0 Hasta total_clientes-1 Hacer
						Escribir 'Cliente ', i+1, ': ', clientes
					FinPara
				FinSi
			5:
				Si total_ventas<100 Entonces
					Escribir 'Ingrese la descripción de la venta: '
					Leer ventas
					total_ventas <- total_ventas+1
					Escribir 'Venta registrada.'
				FinSi
			6:
				Si total_ventas=0 Entonces
					Escribir 'No hay ventas registradas.'
				SiNo
					Para i<-0 Hasta total_ventas-1 Hacer
						Escribir 'Venta ', i+1, ': ', ventas
					FinPara
				FinSi
			7:
				Escribir 'Saliendo del sistema...'
			De Otro Modo:
				Escribir 'Opción no válida.'
		FinSegún
	FinMientras
FinAlgoritmo

Funcion SinTitulo
	
FinFuncion
