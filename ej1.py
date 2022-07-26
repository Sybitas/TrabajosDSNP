# -*- coding: utf-8 -*-
"""
Created on Tue May 10 12:14:49 2022

@author: lab
"""
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido ")
ubicacion=input("Ingrese su ubicacion ")
edad=input("Ingrese su edad ")
space=" "
if edad >=1 and edad <=17:
    print("Es menor de edad")
elif edad >=18 and edad <=25:
    print("Edad media")
elif edad >=25 and edad <=45:
    print("Adulto")
elif edad >=45 and edad <=90:
    print("Tercera edad")
print("Su nombre es: "+nombre+space+apellido+space+" su ubicacion es "+space+ubicacion+space+" su edad es "+space+edad+space)
