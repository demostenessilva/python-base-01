#!/usr/bin/env python3
"""Dicionário Offline com Tradução - Bloco de Notas para Consultas
Versão 0.2.0

Funcionalidades:
    - Adicionar uma nova tradução (comando "new")
    - Consulta exata por palavra (comando "read")
    - Pesquisa por parte do texto ou tradução (comando "search")
    - Listagem completa das entradas (comando "list")
    - Remoção de entradas (comando "remove")
    - Edição de entradas (comando "edit")

Uso:
    Para adicionar uma nova tradução:
        python3 offline_dict.py new <palavra> [<código_do_idioma>]
    Para consultar uma tradução exata:
        python3 offline_dict.py read <palavra>
    Para pesquisar por parte do texto ou tradução:
        python3 offline_dict.py search <termo>
    Para listar todas as entradas:
        python3 offline_dict.py list
    Para remover uma entrada:
        python3 offline_dict.py remove <palavra>
    Para editar uma entrada:
        python3 offline_dict.py edit <palavra>
"""

import os
import sys
from googletrans import Translator

# Comandos aceitos
cmds = ("read", "new", "list", "remove", "edit", "search")

# Caminho do arquivo que armazenará as traduções (dicionário offline)
path = os.curdir
filepath = os.path.join(path, "notes.txt")


def load_entries():
    """Carrega todas as entradas do arquivo e retorna uma lista de dicionários."""
    entries = []
    if not os.path.exists(filepath):
        return entries
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue  # Ignora linhas vazias
            parts = line.strip().split("\t")
            if len(parts) != 3:
                continue  # Ignora linhas malformadas
            entry = {"word": parts[0], "lang": parts[1],
                     "translation": parts[2]}
            entries.append(entry)
    return entries


def save_entries(entries):
    """Salva todas as entradas no arquivo, substituindo o conteúdo existente."""
    with open(filepath, "w", encoding="utf-8") as file:
        for entry in entries:
            file.write(
                "\t".join([entry["word"], entry["lang"], entry["translation"]]) + "\n")


def add_entry(word, target_lang, translation_text):
    """Adiciona uma nova entrada ao arquivo."""
    with open(filepath, "a", encoding="utf-8") as file:
        file.write("\t".join([word, target_lang, translation_text]) + "\n")


def display_entry(entry):
    """Exibe uma entrada formatada."""
    print(f"Palavra: {entry['word']}")
    print(f"Idioma: {entry['lang']}")
    print(f"Tradução: {entry['translation']}")
    print("-" * 30)


def list_entries():
    """Lista todas as entradas do dicionário offline."""
    entries = load_entries()
    if not entries:
        print("Nenhuma entrada encontrada.")
        return
    for entry in entries:
        display_entry(entry)


# Captura dos argumentos da linha de comando
arguments = sys.argv[1:]
if not arguments:
    print(f"Uso: {sys.argv[0]} [read|new|list|remove|edit|search] [args]")
    sys.exit(1)

command = arguments[0]
if command not in cmds:
    print(f"Comando inválido: {command}")
    sys.exit(1)

# Comando: Consulta exata por palavra
if command == "read":
    if len(arguments) < 2:
        print("Erro: Informe a palavra para consulta.")
        sys.exit(1)
    query = arguments[1].lower()
    entries = load_entries()
    found = False
    for entry in entries:
        if entry["word"].lower() == query:
            display_entry(entry)
            found = True
    if not found:
        print("Nenhuma entrada encontrada para a palavra informada.")

# Comando: Adicionar uma nova tradução
elif command == "new":
    if len(arguments) < 2:
        print("Erro: Palavra necessária para tradução.")
        sys.exit(1)
    word = arguments[1]
    if len(arguments) >= 3:
        target_lang = arguments[2]
    else:
        target_lang = input(
            "Código do idioma para tradução (ex: en para inglês): ").strip()

    translator = Translator()
    try:
        translation_obj = translator.translate(
            word, src="pt", dest=target_lang)
        translation_text = translation_obj.text
        print(f"Tradução de '{word}' para '{target_lang}': {translation_text}")
    except Exception as e:
        print("Erro ao traduzir:", e)
        sys.exit(1)

    add_entry(word, target_lang, translation_text)

# Comando: Listar todas as entradas
elif command == "list":
    list_entries()

# Comando: Remover entrada(s) com a palavra informada
elif command == "remove":
    if len(arguments) < 2:
        print("Erro: Informe a palavra para remoção.")
        sys.exit(1)
    query = arguments[1].lower()
    entries = load_entries()
    new_entries = [
        entry for entry in entries if entry["word"].lower() != query]
    if len(entries) == len(new_entries):
        print("Nenhuma entrada encontrada para remoção.")
    else:
        save_entries(new_entries)
        print(f"Entrada(s) com a palavra '{query}' removida(s).")

# Comando: Editar uma entrada existente
elif command == "edit":
    if len(arguments) < 2:
        print("Erro: Informe a palavra para edição.")
        sys.exit(1)
    query = arguments[1].lower()
    entries = load_entries()
    found = False
    for i, entry in enumerate(entries):
        if entry["word"].lower() == query:
            print("Entrada encontrada:")
            display_entry(entry)
            new_word = input(f"Novo valor para a palavra (ou Enter para manter '{
                             entry['word']}'): ").strip()
            new_lang = input(f"Novo código de idioma (ou Enter para manter '{
                             entry['lang']}'): ").strip()
            new_translation = input(f"Nova tradução (ou Enter para manter '{
                                    entry['translation']}'): ").strip()
            if new_word:
                entry["word"] = new_word
            if new_lang:
                entry["lang"] = new_lang
            if new_translation:
                entry["translation"] = new_translation
            entries[i] = entry
            found = True
            print("Entrada atualizada:")
            display_entry(entry)
            break
    if found:
        save_entries(entries)
    else:
        print("Nenhuma entrada encontrada para edição.")

# Comando: Pesquisa parcial (por parte do texto na palavra ou tradução)
elif command == "search":
    if len(arguments) < 2:
        print("Erro: Informe o termo para pesquisa.")
        sys.exit(1)
    search_term = arguments[1].lower()
    entries = load_entries()
    found = False
    for entry in entries:
        if search_term in entry["word"].lower() or search_term in entry["translation"].lower():
            display_entry(entry)
            found = True
    if not found:
        print("Nenhuma entrada encontrada contendo o termo informado.")
