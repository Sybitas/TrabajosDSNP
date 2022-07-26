#Chocolates
#Autor: David Vélez
chocolates=int(input('Ingrese el numero de chocolates fabricados en una dia:'))
cajas=int(chocolates/15)
sobrantes=chocolates %(15)
print('El numero de cajas son',cajas)
print('Los sobrantes son:',sobrantes)