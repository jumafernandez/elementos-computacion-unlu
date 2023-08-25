# -*- coding: utf-8 -*-
"""
TP05, ejercicio 9:
Escribir una función que ingresando el precio de un artículo y la cantidad de dinero 
con el que paga el cliente, retorne el vuelto utilizando la menor cantidad de billetes 
posibles (se cuenta con billetes de 50, 20, 10, 5, 2 y 1).
"""


def vuelto_compra(precio, pago):
    """
    Esta función calcula el vuelto en función del precio y la forma de pago de un artículo

    Parameters
    ----------
    precio : int
        Precio del bien
    pago : int
        Forma de pago

    Returns
    -------
    billete_50 : int
        Vuelto de la compra
        
    billete_20 :
    """
    
    resto = pago - precio
    
    billete_50 = resto // 50
    resto = resto % 50

    billete_20 = resto // 20
    resto = resto % 20

    billete_10 = resto // 10
    resto = resto % 10

    billete_5 = resto // 5
    resto = resto % 5

    billete_2 = resto // 2

    billete_1 = resto % 2

    
    return billete_50, billete_20, billete_10, billete_5, billete_2, billete_1

# Ejemplo de uso
precio_producto = 75
dinero_del_cliente = 150
b50, b20, b10, b5, b2, b1 = vuelto_compra(precio_producto, dinero_del_cliente)

print("$50:", b50)
print("$20:", b20)
print("$10:", b10)
print("$5:", b5)
print("$2:", b2)
print("$1:", b1)
