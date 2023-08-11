# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:52:39 2023

@author: Juan
"""

suma = 0
cantidad = 10

for i in range(cantidad):
    nota = input("Ingrese la nota del alumno ")
    suma += int(nota)
    
promedio = suma/cantidad

print("EL promedio de calificaciones es", promedio)