''' DESAFIO 005 - Faça um programa que leia um número inteiro e mostre na tela
o seu sucessor e antecessor.

'''
msg = 'DESAFIO 005 - PYTHON 3'
print('*************** {} ***************'.format(msg))
print('')
numero = int(input('Digite um número: '))
print('O número {} tem como seu antecessor {} e seu sucessor {}'.format(numero, numero-1, numero+1))
