import time
import math

def num():
    
    global num1, num2
    time.sleep(1/4)
    num1=int(input('Ingrese el primer número:'))
    time.sleep(1/4)
    num2=int(input('Ingrese el segundo número:'))
def numsqrt():
    global num
    time.sleep(1/4)
    num=int(input('Ingrese un número:'))
    
def numexp():
    global num
    time.sleep(1/4)
    num=int(input('Ingrese el exponente de la base:'))
    
def numpow():
    global base,num
    time.sleep(1/4)
    base=int(input('Ingrese la base de la potencia:'))
    time.sleep(1/4)
    num=int(input('Ingrese el exponente de la base:'))
    
def numlog():
    global base,num
    time.sleep(1/4)
    base=int(input('Ingrese la base del logaritmo:'))
    time.sleep(1/4)
    num=int(input('Ingrese el argumento del logaritmo:'))

def numln():
    global num   
    time.sleep(1/4)
    num=int(input('Ingrese el argumento del logaritmo:'))
    
def sumar(a,b):
    time.sleep(1/4)
    print('La suma de ',a,' + ',b,' = ',a+b)

def restar(a,b):
    time.sleep(1/4)
    print('La resta de ',a,' - ',b,' = ',a-b)
        
def multiplicacion(a,b):
    time.sleep(1/4)
    print('La multiplicación de ',a,' x ',b,' = ',a*b)
        
def division(a,b):
    
        if b==0:
            time.sleep(1/4)
            print('No se puede dividir entre cero')
        else:
            time.sleep(1/4)
            print('La división de ',a,' / ',b,' = ',a/b)
def raiz(a):
    
    time.sleep(1/4)
    if a<0:
        print('No se puede sacar la raíz cuadrada de un número negativo')
    else:
        time.sleep(1/4)
        print('La raíz cuadrada de ',a,' = ',math.sqrt(a))
def exp(a):
    time.sleep(1/4)
    print('El resultado de la potencia de e elevado a la',a,' = ',math.exp(a))

def pot(a,b):
    time.sleep(1/4)
    print('El resultado de la potencia de ',a,'elevado a la',b,' = ',math.pow(a, b))

def logar(a,b):
    time.sleep(1/4)
    print('El resultado del logaritmo de base ',a,'de',b,' = ',math.log(a,b))

def ln(a):
    time.sleep(1/4)
    print('El resultado del logaritmo natural de',a,' = ',math.log(a))


def exponencialylogaritmica():
    eleccion=0
    while True:
        time.sleep(1/2)
        print('''
        Ingrese la operación exponencial que quiere realizar:
        
        1) Potencia de base e 
        2) Potencia de cualquier base
        3) Logaritmo 
        4) Logaritmo natural   
        5) Volver
        ''')
        eleccion=int(input(':')) 
        time.sleep(1/8)
        if eleccion==1:
            numexp()  
            exp(num)
        elif eleccion==2:
            numpow()
            pot(base,num)
        elif eleccion==3:
            numlog()
            logar(base,num)
        elif eleccion==4:
            numln()
            ln(num)
        elif eleccion==5:
            break
        
def val ():
    global f,c
    f=int(input('Ingrese el número de filas de la matriz:'))
    c=int(input('Ingrese el número de columnas de la matriz:'))
    while True:
        if f>0 and c>0:
            
            break
        else:
            print('Error el dato ingresado debe ser mayores de 0')
    
def crearm(c,f):  
    global m
    m=[]
    for i in range(f):
        m.append([0])     
        for j in range(c-1):
            m[i].append(0)
    print('Llene la matriz')
    for i in range (0,f):
        for j in range(0,c):
            
            print('M',i+1,' x ',j+1,' : ',end=' ')
            m[i][j]=input()
    print('')
    for i in range (0,f):
        for j in range(0,c):
                
            print('/',m[i][j],end=' ''/')
            
        print(' ')
    
    print(' \n')   
        
        
    print('')
    for i in range (0,f):
        for j in range(0,c):
                
            print('/',m[i][j],end=' ''/')
            
        print(' ')
    
    print(' \n')   
    return(m)    
def diagonal(m):
    if f!=c:
        print('Debe ser una matriz cuadrada')
    else:
        for i in range (0,f):
            for j in range(0,c):             
                        if i==j:
                          print("/",m[i][j],"/",end=" ")
                        else:
        
                           print("/","- ","/",end=" ")
            print("")
                       
          
        
        print(' \n')         
        for i in range (0,f):
             for j in range (0,c):
              if i+j==f-1:
               print("/",m[i][j],"/",end=" ")
              else:
        
                print("/","- ","/",end=" ")
             print("")         
def matriz():
          
           while True:
               val ()
               crearm(c,f)
               while True:
                   time.sleep(1/2)
                   print('''
                   Ingrese la operación exponencial que quiere realizar:
                   
                   1) Encontrar el las diagonales de la matriz
                  
                   2) Volver
                   ''')
                   eleccion=int(input(':')) 
                   time.sleep(1/8)
                   if eleccion==1:
                       diagonal(m)
                   elif eleccion==2:
                       break     
            
elec=0

while True:
    time.sleep(1/2)
    print('''
    Ingrese la operación a realizar:
    
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Exponencial y logaritmica
    6) Raíz
    7) Matrices
    8) Salir de la calculadora 
    ''')
    
    elec=int(input(':'))
    
    time.sleep(1/4)
    if elec==1:
        num()
        sumar(num1,num2)
    
   
    elif elec==2:
        num()
        restar(num1,num2)
   
     
    elif elec==3:
        num()
        multiplicacion(num1,num2)
      
    elif elec==4:
        num()
        division(num1,num2)
    elif elec==5:
        exponencialylogaritmica()
    elif elec==6:
        numsqrt()
        raiz(num)  
    elif elec==6:
        matriz()
    elif elec==8:
        print('Fin de la operación')
        break

    