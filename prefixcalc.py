#!/usr/bin/env python3
"""
Calculadora Prefixada.

Funcionamento:
A calculadora aceita operações prefixadas, onde a operação é especificada antes dos operandos. 
Ela pode ser usada tanto via linha de comando quanto de forma interativa.

Uso via linha de comando:
    [operação] [n1] [n2]

Uso interativo:
    Quando executada sem argumentos, a calculadora solicitará a operação e os valores.

Operações suportadas:
    sum -> Soma (+)
    sub -> Subtração (-)
    mul -> Multiplicação (*)
    div -> Divisão (/)

Exemplos de uso:
    $ prefixcalc.py sum 5 2
    7

    $ prefixcalc.py mul 10 5
    50

    $ prefixcalc.py
    operação: sum
    n1: 5
    n2: 4
    9

Resultados:
    Os resultados das operações são salvos em um arquivo de log chamado `Prefixcal.log` no diretório atual.

Versão:
    Versão atual: 0.1.0
"""

# Importações necessárias
import os
import sys

from datetime import datetime

# Versão do programa
__version__ = "0.1.0"

# Obtém os argumentos passados na linha de comando, ignorando o primeiro (nome do script)
arguments = sys.argv[1:]

# Verifica se não há argumentos passados
if not arguments:
    # Se não houver, solicita ao usuário que insira a operação e os números
    operation = input("Operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    # Armazena os valores inseridos em uma lista chamada `arguments`
    arguments = [operation, n1, n2]
# Verifica se o número de argumentos é diferente de 3
elif len(arguments) != 3:
    # Se for diferente, exibe uma mensagem de erro e encerra o programa
    print("Número de argumentos inválidos")
    print("Exemplo de uso: `sum 5 5`")
    sys.exit(1)  # Encerra o programa com código de erro 1

# Separa a operação e os números da lista de argumentos
operation, *nums = arguments

# Lista de operações válidas
valid_operations = ("sum", "sub", "mul", "div")

# Verifica se a operação fornecida está na lista de operações válidas
if operation not in valid_operations:
    print("Operação inválida")
    print(f"Operações válidas: {valid_operations}")
    sys.exit(1)  # Encerra o programa com código de erro 1

# Lista para armazenar os números validados
validated_nums = []

# Itera sobre os números fornecidos
for num in nums:
    # Verifica se o número é válido (permite números inteiros ou decimais)
    if not num.replace(".", "").isdigit():
        print(f"Número inválido: {num}")
        sys.exit(1)  # Encerra o programa com código de erro 1

    # Converte o número para float (se tiver ponto decimal) ou int (caso contrário)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    # Adiciona o número validado à lista `validated_nums`
    validated_nums.append(num)

# Atribui os números validados às variáveis n1 e n2
n1, n2 = validated_nums

# Realiza a operação matemática com base na operação fornecida
if operation == "sum":
    result = n1 + n2  # Soma
elif operation == "sub":
    result = n1 - n2  # Subtração
elif operation == "mul":
    result = n1 * n2  # Multiplicação
elif operation == "div":
    result = n1 / n2  # Divisão

# Define o caminho do arquivo de log
path = os.curdir
filepath = os.path.join(path, "prefixcal.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")


# Salva a operação e o resultado no arquivo de log
with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")

# Exibe o resultado da operação
print(f"O resultado é {result}")
