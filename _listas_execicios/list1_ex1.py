# 1. Desenvolva o algoritmo de um programa onde o usuário irá informar um número
# inteiro e o programa deve calcular e exibir o número imediatamente antecessor ao
# número digitado pelo usuário.

num = int(input('Digite um número inteiro: '))
antecessor = num - 1
print('O antecessor do seu número é {}:'.format(antecessor))
