from numpy as np
from pandas as pd

tickets = []
while True:
    print('1- Adicionar')
    print('2- Listar')
    print('6- Sair')
    escolha = input('Selecione uma opção')
    
    if escolha == "1":
        cliente = input('Qual o nome do cliente?')
        problema = input('Qual o problema?')
        tickets.append(cliente, problema)
        print(f'{cliente} adicionado na lista')
    elif escolha == "2":
        for item in tickets:
            print(item)
    elif escolha == "6":
        break
    else:
        print('Opção invalida')
