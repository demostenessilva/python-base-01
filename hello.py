#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da Lingua configurada no ambiente, o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, por exemplo:

   export LANG=pt_BR

Ou informe a linguagem através do argumento de linha de comando `--lang=pt_BR`.

Ou o usuário terá que digitar o idioma manualmente.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""

import os
import sys

__version__ = "0.2.0"
__author__ = "Silva"
__license__ = "Unlicense"

# Dicionário para armazenar os argumentos passados via linha de comando
arguments = {"lang": None, "count": 1}

# Processa os argumentos passados via linha de comando
for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")  # Divide argumento no formato chave=valor
        key = key.lstrip("-").strip()
        value = value.strip()
        if key not in arguments:
            raise ValueError(f"Opção inválida `{key}`")
        arguments[key] = value
    except ValueError:
        print(f"Erro: Argumento inválido `{
              arg}`. Use o formato `chave=valor`.")
        sys.exit(1)

# Dicionário com as mensagens de "Hello World" em diferentes idiomas
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola Mundo!",
    "fr_FR": "Bonjour Monde",
}


def get_language():
    """Obtém o idioma do ambiente ou solicita ao usuário."""
    lang = os.getenv("LANG", input("Qual o seu idioma:").strip()).split(".")[0]
    return lang if lang in msg else "en_US"


# Determina o idioma atual com base nos argumentos ou variáveis de ambiente
current_language = arguments["lang"] or get_language()

# Verifica se count é um número válido
try:
    count = int(arguments["count"])
    if count < 1:
        raise ValueError
except ValueError:
    print("Erro: O argumento 'count' deve ser um número inteiro positivo.")
    sys.exit(1)

# Exibe a mensagem correspondente ao idioma configurado
print("\n".join([msg.get(current_language, "Hello, World!")] * count))
