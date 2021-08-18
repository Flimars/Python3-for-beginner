''' Curso em Vídeo: Aula 06 Tipos primitivos e print.format
    Curso de Programação em Python

    The Python language created in 1991 by Guido Van Rossum.
    Aiming at productivity and readability.
'''
# Entrada(input) de dados concatenando(unindo) duas Strings(texto e/ou caracteres) em python:
n = input('Digite um valor: ') # Recebe uma string 'que representa número'. Ex: '6'.
m = input('Digite outro valor: ') # Tmb recebe uma string 'que representa número'. Ex: '6'.
nom = n + m  # Temos aqui a concatenação dos valores  de duas strings.
# SAÍDA: Concatenação de strings (6+6)= 66.
print('A soma vale ', nom, 'ERRADO!') # E não a soma de dois números inteiros = 12.
print('')
print('////////////////////////////////////////////////////////////////////////////////////')
#  Entrada(input) de dados somando dois números inteiros em python:
x = int(input('Informe um número para X: ')) # O tipo primitivo 'int' realiza uma coerção(força) da string para inteiro.
y = int(input('Informe um número para Y: '))
soma = x + y
print('A soma entre {} e {} é = {}'.format(x, y, soma))
print('////////////////////////////////////////////////////////////////////////////////////')