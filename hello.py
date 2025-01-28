#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da Lingua configurada no ambiente, o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, por exemplo:

   export LANG=pt_BR

Ou informe a linguagem através do argumento de linha de comando `--lang`.

Ou o usuário terá que digitar o idioma manualmente.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"  # Versão do programa
__author__ = "Silva"   # Autor do programa
__license__ = "Unlicense"  # Licença do programa

import os
import sys

# Dicionário para armazenar os argumentos passados via linha de comando
arguments = {"lang": None, "count": 1}

# Processa os argumentos passados via linha de comando
for arg in sys.argv[1:]:
    # TODO: Tratar ValueError (caso o argumento não esteja no formato chave=valor)
    key, value = arg.split("=")
    key = key.lstrip("-").strip()  # Remove hífens e espaços em branco da chave
    value = value.strip()  # Remove espaços em branco do valor
    if key not in arguments:
        # Mensagem de erro para opções inválidas
        print(f"Opção invalida `{key}`")
        sys.exit()  # Encerra o programa se uma opção inválida for detectada
    arguments[key] = value  # Atualiza o valor no dicionário de argumentos

# Determina o idioma atual com base nos argumentos ou variáveis de ambiente
current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição para evitar código duplicado
    if "LANG" in os.environ:
        # Obtém o idioma da variável de ambiente LANG
        current_language = os.getenv("LANG")
    else:
        # Solicita ao usuário que insira o idioma
        current_language = input("Qual o seu idioma:")

# Limita o idioma aos primeiros 5 caracteres (ex: "pt_BR" -> "pt_BR")
current_language = current_language[:5]

# Dicionário com as mensagens de "Hello World" em diferentes idiomas
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola Mundo!",
    "fr_FR": "Bonjour Monde",
}

# Exibe a mensagem correspondente ao idioma configurado, repetida conforme o valor de "count"
print(msg[current_language] * int(arguments["count"]))
