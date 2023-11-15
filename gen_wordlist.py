import random
import string
import os

CHARSETS = {"en": "abcdefghijklmnopqrstuvwxyz", "pt": "abcdefghijklmnopqrstuvwxyzáéíóúâêôãõç"}

def generate_wordlist(length, min_length, max_length, language, include_numbers, include_symbols):
  """
  Gera uma lista de palavras com o comprimento especificado.

  Args:
    length: O comprimento da lista de palavras.
    min_length: O comprimento mínimo de uma palavra.
    max_length: O comprimento máximo de uma palavra.
    language: O idioma das palavras a serem geradas.
    include_numbers: Se verdadeiro, inclui números nas palavras.
    include_symbols: Se verdadeiro, inclui símbolos nas palavras.

  Returns:
    Uma lista de palavras.
  """

  if min_length > max_length:
    raise ValueError("O comprimento mínimo deve ser menor ou igual ao comprimento máximo.")

  charset = CHARSETS[language]

  if include_numbers:
    charset += string.digits

  if include_symbols:
    charset += string.punctuation

  return [random.choice(charset) for _ in range(length)]

def save_wordlist(wordlist):
  """
  Salva a wordlist em um arquivo.

  Args:
    wordlist: A lista de palavras a ser salva.
  """

  path = "/tmp/wordlists"
  if not os.path.exists(path):
    os.mkdir(path)

  with open(path + "/wordlist.txt", "w") as f:
    buffer = ""
    for word in wordlist:
      buffer += word + "\n"
    f.write(buffer)

import logging

def main():
  """
  Interação com o usuário para gerar uma wordlist.
  """

  logging.basicConfig(level=logging.INFO)

  # Menu

  print("Gen_Wordlist_")
  print("By gabs77u")
  print("Selecione uma opção:")
  print("1. Gerar wordlist")
  print("2. Visualizar wordlist")
  print("3. Sair")

  option = input("Opção: ")

  # Processamento da opção

  while option != "3":

    # Opção de gerar wordlist

    if option == "1":

      # Solicita as informações da wordlist

      length = int(input("Informe o comprimento da lista de palavras: "))
      min_length = int(input("Informe o comprimento mínimo de uma palavra: "))

      while min_length < 1:
        logging.error("O comprimento mínimo deve ser um número inteiro positivo.")
        min_length = int(input("Informe o comprimento mínimo de uma palavra: "))

      max_length = int(input("Informe o comprimento máximo de uma palavra: "))

      while max_length < 1 or max_length < min_length:
        logging.error("O comprimento máximo deve ser um número inteiro positivo e maior ou igual ao comprimento mínimo.")
        max_length = int(input("Informe o comprimento máximo de uma palavra: "))

      language = input("Deseja gerar palavras em inglês (en) ou português (pt)? (en/pt): ")
      include_numbers = input("Incluir números nas palavras (s/n)? ") == "s"
      include_symbols = input("Incluir símbolos nas palavras (s/n)? ") == "s"

      # Gera a wordlist

      try:
        wordlist = generate_wordlist(length, min_length, max_length, language, include_numbers, include_symbols)
      except ValueError as e:
        logging.error(e)
        continue

      # Salva a wordlist

      save_wordlist(wordlist)

      # Exibe a mensagem de geração bem-sucedida

      print("Wordlist gerada.")

    # Opção de visualizar wordlist

    elif option == "2":

      # Exibe a wordlist

      print("Deseja visualizar a wordlist? (s/n) ")

      if input() == "s":
        for word in wordlist:
          print(word)

    else:
      # Opção de sair

      print("Saindo...")

if __name__ == "__main__":
  main()