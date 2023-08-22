# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 08:14:01 2023

@author: Juan
"""

numeros = 0
candidato = 1

while numeros < 10:
    
    candidato = candidato + 1
    sumatoria = 0
    for posible_divisor in range(1, candidato):
        if candidato % posible_divisor == 0:
            print(posible_divisor)
            sumatoria = sumatoria + posible_divisor
    
    if sumatoria == candidato:
        numeros = numeros + 1
        print(f'Número perfecto {numeros}: {candidato}')
