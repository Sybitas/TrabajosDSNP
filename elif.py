# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:42:55 2022

@author: lab
"""
acl=int(input("Ingrese el # de ACL"))
if acl >=1 and acl <=99:
    print("ACL ES ESTANDAR")
elif acl >=100 and acl <=199:
    print("ACL ES EXTENDIDA")
else:
    print("El dato ingresado no es un ACL")
    
    