# faça o computador jogar jokenpo
from random import choice
import time
print('\033[35m='*30,'\033[m')
print('JOKENPÔ')
print('\033[35m='*30,'\033[m')
lista = ['pedra', 'papel', 'tesoura']
computador = str(choice(lista))
jogador = input('pedra, papel ou tesoura? ').upper()
time.sleep(1)
print('Perai to pensando')
time.sleep(2)
if jogador == 'PEDRA' and computador == 'pedra':
    print('Caramba, deu empate. Meu criador não vai gostar nada disso. Pedra de merda.')
if jogador == 'PEDRA' and computador == 'papel':
    print('HAHAHA, como esperado, eu ganhei. Humano inferior. Papel sempre funciona.')
if jogador == 'PEDRA' and computador == 'tesoura':
    print('Eu perdi? Meu Deus Meu Deus eu estou defeituoso! Por favor não me desmonta! Eu sei que posso fazer melhor!\n'
          'Nunca mais escolho tesoura.')
if jogador == 'PAPEL' and computador == 'pedra':
    print('Eu perdi? Meu Deus Meu Deus eu estou defeituoso! Por favor não me desmonta! Eu sei que posso fazer melhor!\n'
          'Nunca mais escolho pedra.')
if jogador == 'PAPEL' and computador == 'papel':
    print('Caramba, deu empate, também escolhi papel. Meu criador não vai gostar nada disso.')
if jogador == 'PAPEL' and computador == 'tesoura':
    print('HAHAHA, como esperado, eu ganhei. Humano inferior. Tesoura sempre funciona.')
if jogador == 'TESOURA' and computador == 'pedra':
    print('HAHAHA, como esperado, eu ganhei. Humano inferior. Pedra sempre funciona.')
if jogador == 'TESOURA' and computador == 'papel':
    print('Eu perdi? Meu Deus Meu Deus eu estou defeituoso! Por favor não me desmonta! Eu sei que posso fazer melhor!\n'
          'Nunca mais escolho papel.')
if jogador == 'TESOURA' and computador == 'tesoura':
    print('Caramba, deu empate, também escolhi papel. Meu criador não vai gostar nada disso.')








