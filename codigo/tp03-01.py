# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:56:24 2023

@author: Juan
"""

suma = 0
producto = 1

for numero in range(20, 501, 2):
    suma = suma + numero
    producto = producto * numero

print(f"La suma es {suma}")
print(f"El producto es {producto}")
