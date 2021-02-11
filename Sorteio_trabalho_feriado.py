from random import choice
from time import sleep

sorteado = []
lista_nome = []

# Adicionar nomes
while True:
    nome = str(input('Digite o nome: ')).strip().capitalize()

    # Adicionar na lista_nome
    if nome not in lista_nome:
        lista_nome.append(nome)

    # Flag de parada
    adicionar = ''
    while 'S' != adicionar != 'N':
        adicionar = str(input('Adicionar? [S/N]: ')).strip().upper()[0]
    if adicionar == 'N':
        break

print('=' * 40)

quantidade = int(input('\nQuantidade de sorteados: '))

# Realizar o sorteio
cont = 0
while True:
    sorteio = choice(lista_nome)

    if sorteio not in sorteado:
        sorteado.append(sorteio)
        cont += 1

    if cont >= quantidade:
        break

print('=' * 40)

# Exibir ganhadores
for ganhador in sorteado:
    sleep(1)
    print(ganhador)

print('=' * 40)

sleep(10)
