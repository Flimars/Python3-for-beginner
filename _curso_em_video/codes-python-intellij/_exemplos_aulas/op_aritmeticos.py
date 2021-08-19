''' Curso em Vídeo: Aula 07 Trabalhando Operadores Aritméticos
    Curso de Programação em Python

    The Python language created in 1991 by Guido Van Rossum.
    Aiming at productivity and readability.
'''
print('*********************************************************************************')
print('********************* Operadores Aritméticos em Python **************************')
print('*********************************************************************************')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
multi = n1 * n2
divisao = n1 / n2
divint = n1 // n2
expon = n1 ** n2
print('A Soma é {}, Multiplicação é {} e a Divisão é {:.3f}'.format(soma, multi, divisao), end=' ')
print('Divisão inteira é {}, Potência é {}'.format(divint, expon))
print('')
print('A Soma é {},\n Multiplicação é {} e a\n Divisão é {:.3f}'.format(soma, multi, divisao))
print('Divisão inteira é {},\n Potência é {}'.format(divint, expon))
print('')
print('A Soma é {}, Multiplicação é {} e a Divisão é {:.3f}'.format(soma, multi, divisao))
print('Divisão inteira é {}, Potência é {}'.format(divint, expon))
