# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 20:10:47 2023

@author: Juan
"""

op = input("Ingrese una operación (o salir para terminar el programa): ")

while (op!="salir"):
    
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))

    if (op=="+"):
        resultado = n1+n2
    elif (op == "-"):
        resultado = n1-n2
    elif (op == "*"):
        resultado = n1*n2
    elif (op == "/"):
        resultado = n1/n2
    else:
        print("Operación no valida.")    
    
    print(f"\n{n1} {op} {n2} = {resultado}")
    
    op = input("Ingrese una operación (o salir para terminar el programa): ")
