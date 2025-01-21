#!/usr/bin/env python3
""" Imprimir a tabuada do 1 ao 10."""
__version__ = "0.1.0"
__author__ = "Silva"

# numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterable (percorriveis)

# para cada numero em numeros:
for numero in numeros:
    print("Tabuado do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-" * 12)

# String (corda de caracteres, corrente)
# Tabela ASCII
# Concatenação
# Interpolação
