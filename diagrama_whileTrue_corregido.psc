Algoritmo sin_titulo
	numero1 <- 100
	sumainter <- 0
	contador1 <- 0
	contador2 <- 0
	suma1 <- 0
	Repetir
		Escribir 'Ingrese el primer número:'
		Leer n1
		Escribir 'Ingrese el segundo número:'
		Leer n2
		Si n1=n2 Entonces
			Escribir 'Error los números son iguales'
		FinSi
	Hasta Que n1<>n2
	
	Si n1>n2 Entonces
		minimo <- n2
		maximo <- n1
	SiNo
		minimo <- n1
		maximo <- n2
	FinSi
	Repetir
		Escribir "Digite un numero: "
		leer numero1
		Si numero1=0
		Fin Si
	Hasta Que n1<>n2
	Si numero1<>0 Entonces
		Escribir "Puedo continuar"
	Fin Si
FinAlgoritmo
