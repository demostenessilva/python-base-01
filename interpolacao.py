import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit()

filename = arguments[0]
templatename = arguments[1]
path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


clientes = []

for line in open(filepath):
    name, email = line.split(",")

    print(f"Enviando email para:{email}")
    print()
    print(open(templatepath).read() % {"nome": name, "produto": "caneta", "texto": "Escrever muito bem",
          "link": "https://canetaslegais.com", "quantidade": 1, "preco": 50.5, })

    print("-" * 50)
