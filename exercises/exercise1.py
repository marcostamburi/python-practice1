"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""
"""
lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado=lado_cuadrado*lado_cuadrado
area_cuadrado=pow(lado_cuadrado, 2)
# COMPLETAR - FIN
print(area_cuadrado)

assert area_cuadrado == 25
"""

"""
Re-Escribir usando el operador de potencia.


lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado = pow(lado_cuadrado, 2)
# COMPLETAR - FIN
print(area_cuadrado)
assert area_cuadrado == 25
"""

"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado = lado_cuadrado**2
# COMPLETAR - FIN
assert area_cuadrado == 25


"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

# COMPLETAR - INICIO
cantidad_a_comprar = int(presupuesto_disponible/precio)
# COMPLETAR - FIN
assert cantidad_a_comprar == 2


"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

# COMPLETAR - INICIO
if numero_incalculable%7 == 0:
    es_divisible_por_siete = True
# COMPLETAR - FIN

assert es_divisible_por_siete