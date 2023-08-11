def perimetro_rectangulo(base, altura):
    """
    Parameters
    ----------
    base : float
        Es la base del rectángulo
    altura : float
        Es la altura del rectángulo

    Returns
    -------
    Perímetro: float
    """
    resultado = base*2 + altura*2
    
    return resultado

b = 7
a = 5
x = perimetro_rectangulo(b, a)
print(f'El perímetro del rectángulo es {x}')

