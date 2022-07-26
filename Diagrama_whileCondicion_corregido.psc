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
	Mientras numero1<>0 Hacer
		Escribir 'Ingrese un número:'
		Leer numero1
		Si numero1>minimo Y numero1<maximo Entonces
			sumainter <- sumainter+numero1
		FinSi
		Si numero1<minimo O numero1>maximo Entonces
			suma1 <- suma1+numero1
			contador1 <- contador1+1
		FinSi
		Si numero1=minimo O numero1=maximo Entonces
			contador2 <- contador2+1
		FinSi
	FinMientras
	dive <- suma1/contador1
	Escribir 'La suma de los números que estan dentro es:',sumainter
	Escribir 'El promedio de los números fuera del intervalo es:',dive
	Escribir 'La cantidad de los números ingresados iguales a los limit es:',contador2
	Escribir 'fin del programa'
FinAlgoritmo
