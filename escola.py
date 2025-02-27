#!/usr/bin/env python3

""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades
"""
__version__ = "0.1.0"
__author__ = "Silva"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [("Inglês", aula_ingles), ("Dança", aula_danca),
              ("Música", aula_musica)]

# Listar alunos em cada atividade por sala.
for nome_atividade, atividade in atividades:
    print()
    print(f"Alunos da atividade de {nome_atividade}")
    print("-" * 45)
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    print("sala1 ", atividade_sala1)
    print("sala2", atividade_sala2)
    print()
    print("#" * 45)
