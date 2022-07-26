while True: #Se coloca while true para hacer un bucle"
    num1=int(input("Digitar el primer número: ")) #Se ingresa por teclado el primer numero
    num2=int(input("Digite el segundo número: ")) #Se ingresa por teclado el segundo numero
    if num1==num2: #Se asigna if con la condición num1 es igual a num2
        print("Error los numeros son iguales") #Se imprime la condicion del if
    else: #Si la condicion if no se cumple entonces
        break #Se termina el bucle si no se cumple if
if num1>num2: #Se usa if si num1 mayor a num2
    minimo=num2 #Se asigna la variable minimo, con valor igual a num2
    maximo=num1 #Se asigna la variable maximo, con valor igual a num1
else: #Si la condicion if no se cumple entonces
    minimo=num1 #Se asigna la variable minimo, con valor igual a num1
    maximo=num2 #Se asigna la variable maximo, con valor igual a num2
while True: #Se coloca while true para hacer un bucle"
    numero=int(input("Digite un numero: ")) #Se ingresa por teclado un numero
    if numero==0: #Se asigna if con la condición numero es igual a 0
        break #Se termina el bucle 
    else: #Si la condicion if no se cumple entonces
        print("Puedo continuar") #Con un texto se imprime puedo continuar como condicion en else