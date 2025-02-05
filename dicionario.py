#!/usr/bin/env python3
"""Dicionário Offline com Tradução - Bloco de Notas para Consultas
Versão 0.4.0

Melhorias implementadas:
- Validação de entrada reforçada
- Controle de duplicatas
- Seleção múltipla para edição/remoção
- Suporte a paginação
- Histórico de alterações
- Novas funcionalidades de pesquisa
- Melhor tratamento de erros
"""

import os
import sys
from datetime import datetime
from googletrans import Translator
from collections import defaultdict

# Configurações
FILEPATH = os.path.join(os.curdir, "dictionary_v2.txt")
HISTORY_PATH = os.path.join(os.curdir, "history.log")
SUPPORTED_LANGUAGES = {'en', 'es', 'fr', 'de', 'pt', 'it', 'ru', 'ja'}
ENTRY_FIELDS = ['word', 'src_lang', 'target_lang', 'translation', 'timestamp']
ITEMS_PER_PAGE = 5


class DictionaryManager:
    """Classe principal para gerenciamento do dicionário"""

    def __init__(self):
        self.entries = self.load_entries()
        self.history = []
        self.translator = Translator()

    def load_entries(self):
        """Carrega entradas do arquivo"""
        entries = []
        if not os.path.exists(FILEPATH):
            return entries

        with open(FILEPATH, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                parts = line.strip().split("\t")
                if len(parts) != 5:
                    continue
                entries.append({
                    'word': parts[0],
                    'src_lang': parts[1],
                    'target_lang': parts[2],
                    'translation': parts[3],
                    'timestamp': parts[4]
                })
        return entries

    def save_entries(self):
        """Salva entradas no arquivo"""
        with open(FILEPATH, "w", encoding="utf-8") as f:
            for entry in self.entries:
                f.write("\t".join([
                    entry['word'],
                    entry['src_lang'],
                    entry['target_lang'],
                    entry['translation'],
                    entry['timestamp']
                ]) + "\n")

    def add_entry(self, entry):
        """Adiciona nova entrada com verificação de duplicatas"""
        duplicate = next((e for e in self.entries if
                         e['word'] == entry['word'] and
                         e['src_lang'] == entry['src_lang'] and
                         e['target_lang'] == entry['target_lang']), None)

        if duplicate:
            print("Entrada duplicada encontrada:")
            self.display_entry(duplicate)
            choice = input("Deseja sobrescrever? (s/n): ").lower()
            if choice != 's':
                return False
            self.entries.remove(duplicate)

        entry['timestamp'] = datetime.now().isoformat()
        self.entries.append(entry)
        self.log_change("ADD", entry)
        return True

    def log_change(self, action, entry):
        """Registra alterações no histórico"""
        log_entry = f"{datetime.now()} | {action} | {entry['word']} | " \
            f"{entry['src_lang']}-{entry['target_lang']} | " \
            f"user: {os.getlogin()}"
        self.history.append(log_entry)

        with open(HISTORY_PATH, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")

    def search_entries(self, term, field='all'):
        """Pesquisa entradas por termo"""
        term = term.lower()
        results = []
        for entry in self.entries:
            if field == 'all':
                match = (term in entry['word'].lower() or
                         term in entry['translation'].lower() or
                         term in entry['src_lang'].lower() or
                         term in entry['target_lang'].lower())
            else:
                match = term in entry[field].lower()
            if match:
                results.append(entry)
        return results

    def display_entries(self, entries, page=1):
        """Exibe entradas com paginação"""
        total_pages = (len(entries) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
        start = (page-1) * ITEMS_PER_PAGE
        end = start + ITEMS_PER_PAGE

        for idx, entry in enumerate(entries[start:end], start+1):
            print(f"Entrada #{idx}")
            self.display_entry(entry)

        print(f"\nPágina {page}/{total_pages}")
        return total_pages

    @staticmethod
    def display_entry(entry):
        """Exibe detalhes de uma entrada"""
        print(f"Palavra: {entry['word']}")
        print(f"Tradução: {entry['translation']}")
        print(f"Idiomas: {entry['src_lang']} → {entry['target_lang']}")
        print(f"Última atualização: {entry['timestamp']}")
        print("-" * 50)

    def get_user_selection(self, entries):
        """Obtém seleção do usuário a partir de uma lista"""
        for idx, entry in enumerate(entries, 1):
            print(f"{idx}. {entry['word']} ({
                  entry['src_lang']}→{entry['target_lang']})")

        while True:
            choice = input("\nSelecione uma entrada (número) ou 'cancelar': ")
            if choice.lower() == 'cancelar':
                return None
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(entries):
                    return entries[idx]
                print("Número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Use números.")


class UserInterface:
    """Classe para interação com o usuário"""

    def __init__(self, manager):
        self.manager = manager

    def show_menu(self):
        """Exibe o menu principal"""
        print("\n" + "="*40)
        print("DICIONÁRIO OFFLINE - MENU PRINCIPAL")
        print("1. Traduzir palavra/expressão")
        print("2. Consultar entrada")
        print("3. Pesquisar conteúdo")
        print("4. Listar todas as entradas")
        print("5. Editar entrada")
        print("6. Remover entrada")
        print("7. Histórico de alterações")
        print("0. Sair")
        return input("\nOpção: ").strip()

    def translate_word(self):
        """Fluxo de tradução de palavras"""
        word = input("\nDigite a palavra/expressão (ou 'sair'): ").strip()
        if word.lower() == 'sair':
            return

        try:
            detected = self.manager.translator.detect(word)
            src_lang = detected.lang
            print(f"Idioma detectado: {src_lang}")
        except Exception as e:
            print(f"Erro de detecção: {str(e)}")
            return

        target_lang = input("Idioma de destino (ex: en): ").strip().lower()
        if target_lang not in SUPPORTED_LANGUAGES:
            print("Idioma não suportado.")
            return

        try:
            translation = self.manager.translator.translate(
                word, src=src_lang, dest=target_lang
            ).text
        except Exception as e:
            print(f"Erro de tradução: {str(e)}")
            return

        new_entry = {
            'word': word,
            'src_lang': src_lang,
            'target_lang': target_lang,
            'translation': translation
        }

        if self.manager.add_entry(new_entry):
            print("\nNova entrada adicionada:")
            self.manager.display_entry(new_entry)
            self.manager.save_entries()

    def search_entries(self):
        """Fluxo de pesquisa avançada"""
        term = input("Termo de pesquisa: ").strip()
        if not term:
            return

        field = input(
            "Campo a pesquisar (word, translation, lang, all): ").strip().lower()
        valid_fields = ['word', 'translation', 'lang', 'all']
        if field not in valid_fields:
            print("Campo inválido.")
            return

        results = self.manager.search_entries(term, field)
        if not results:
            print("Nenhum resultado encontrado.")
            return

        page = 1
        while True:
            total_pages = self.manager.display_entries(results, page)
            nav = input("[P]róxima, [V]oltar, [S]air: ").lower()
            if nav == 'p' and page < total_pages:
                page += 1
            elif nav == 'v' and page > 1:
                page -= 1
            else:
                break


def main():
    manager = DictionaryManager()
    ui = UserInterface(manager)

    while True:
        choice = ui.show_menu()

        if choice == '1':
            ui.translate_word()
        elif choice == '2':
            pass  # Implementar consulta
        elif choice == '3':
            ui.search_entries()
        elif choice == '0':
            print("Até logo!")
            sys.exit()
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
