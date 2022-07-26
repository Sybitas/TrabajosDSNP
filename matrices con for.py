# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:29:55 2022

@author: DAVID
"""

matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
filas=3
columna=4
for i in range(filas):
    for j in range(columna):
        print(matrix[i][j],end=" ")
    print(" ")