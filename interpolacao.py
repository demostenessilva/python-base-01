#!/usr/bin/env python3

# Importa os módulos necessários
import os
import sys

# Captura os argumentos passados na linha de comando, excluindo o nome do script
arguments = sys.argv[1:]

# Verifica se os argumentos foram fornecidos
if not arguments:
    print("Informe o nome do arquivo de emails")  # Mensagem de erro
    sys.exit()  # Encerra a execução do script

# Atribui os argumentos às variáveis
filename = arguments[0]
templatename = arguments[1]

# Define o caminho do diretório atual
path = os.curdir

# Cria os caminhos completos para os arquivos de emails e template
filepath = os.path.join(path, filename)
# Caminho do arquivo de template
templatepath = os.path.join(path, templatename)

# Lista para armazenar os clientes (não utilizada no código atual)
clientes = []

# Abre o arquivo de emails e processa cada linha
for line in open(filepath):
    # Divide a linha em nome e email usando a vírgula como separador
    name, email = line.split(",")

    # Simula o envio de um email para o cliente
    print(f"Enviando email para: {email}")
    print()  # Linha em branco para melhorar a legibilidade

    # Lê o conteúdo do template e substitui os placeholders pelos valores correspondentes
    print(
        open(templatepath).read() % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )

    # Exibe uma linha de separação para melhorar a visualização
    print("-" * 50)
