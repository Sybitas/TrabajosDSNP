# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:49:43 2022

@author: lab
"""
lista2=[]
lista3=[]
lista=["R1",
       "R2",
       "R3",
       "S1",
       "S2",
       "S3"]
for item in lista:
    if "R" in item:
        lista2.append(item)
    else:
        lista3.append(item)
