numero=100 #Se asigna la variable "numero", con numero igual a 100
sumainter=0 #Se asigna la variable "sumainter", con numero igual a 0
contador1=0 #Se asigna la variable "contador1", con numero igual a 0
contador2=1 #Se asigna la variable "contador2", con numero igual a 1
suma1=0 #Se asigna la variable "suma1", con numero igual a 0
while True: #Se coloca while true para hacer un bucle"
    num1=int(input("Ingrese el primer número: ")) #Se ingresa por teclado el primer numero
    num2=int(input("Ingrese el segundo número: ")) #Se ingresa por teclado el segundo numero
    if num1==num2: #Se asigna if con la condición num1 es igual a num2
        print("error los numeros son iguales") #Se imprime la condicion del if
    else: #Si la condicion if no se cumple entonces
        break #Se termina el bucle si no se cumple if
if num1>num2: #Se usa if si num1 mayor a num2
    minimo=num2 #Se asigna la variable minimo, con valor igual a num2
    maximo=num1 #Se asigna la variable maximo, con valor igual a num1
else: #Si la condicion if no se cumple entonces
    minimo=num1 #Se asigna la variable minimo, con valor igual a num1
    maximo=num2 #Se asigna la variable maximo, con valor igual a num2
while numero!=0: #Se crea un while, siendo la condicion de un numero distinto a 0
    numero=int(input("ingrese un número ")) #Se ingresa por teclado un numero
    if numero>minimo and numero<maximo: #Se coloca un if con la condicion de numero mayor a minimo y menor a maximo
        sumainter+=numero #Se asigna la variable "sumainter", el valor de sumainter más numero
    elif numero<minimo or numero>maximo: #Se coloca un if con la condicion de numero menor a minimo y mayor a maximo
        suma1+=numero #Se asigna la variable "suma1", el valor de suma1 más numero
        contador1+=1 #Se asigna la variable contador1 como contador1 más 1
    elif numero==minimo or numero==maximo: #Se usa elif si numero es igual a minimo o a maximo 
        contador2+=1 #Se asigna la variable contador1 como contador2 más 1
print("la suma de los numeros quu estan dentro es:",sumainter) #Con un texto se imprime la variable sumainter
print("el promedio de los numeros fuera del intervalo es: ",suma1/contador1) #Con un texto se imprime la variable suma1/contado1
print("la cantidad de los numeros  ingresados iguales a los limites: ",contador2) #Con un texto se imprime la variable contador2
print("fin del programa ") #Con un texto se imprime El fin del programa