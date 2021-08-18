''' DESAFIO 004 - Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possiveis sobre ele.

'''
msg = 'DESAFIO 004 - PYTHON 3'
print('*************** {} ***************'.format(msg))
print('')

valor = input('Digite algo: ')
print('Q tipo primitivo desse valor é: ', type(valor))
print('É escrito com letras maiúsculas ?', valor.isupper())
print('É um número ?', valor.isnumeric())
print('É alfabetico ?', valor.isalpha())
print('Só tem espaços ?', valor.isspace())
print('É escrito com letras minúsculas ?', valor.islower())
print('É um valor alfanumérico ?', valor.islower())






