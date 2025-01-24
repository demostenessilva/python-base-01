#!/usr/bin/env python3
""" Imprimir a tabuada do 1 ao 10.
---Tabuada do 1---

    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
...
##################
---Tabuada do 2---

    2 x 1 = 2
    2 x 2 = 4  
...
###################

"""
__version__ = "0.1.1"
__author__ = "Silva"

# numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range(1, 11))

# Iterable (percorriveis)

# para cada numero em numeros:
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print()
    print("#" * 18)
    print()
    print()


# String (corda de caracteres, corrente)
# Tabela ASCII
# Concatenação %s
# Interpolação
# str.format {}
# print("\u0001F353") --> incluir emojis no código
