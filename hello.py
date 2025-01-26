#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da Lingua configurada no
ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

   export LANG=pt_BR

Execução: 

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Silva"
__license__ = "Unlicense"

import os
# Padrão snake case
current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá Mundo!",
    "it-IT": "Ciao, Mondo!",
    "es_SP": "Hola Mundo!",
    "fr_FR": "Bonjour Monde",
}
# sets (Hash Table) - O(1) - constante
# dict (Hash Table)

# Ordem de complexidade o(n)


print(msg[current_language])
