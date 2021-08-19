''' Curso em Vídeo: Aula 04 Trabalhando Primeiros comandos com variáveis
    Curso de Programação em Python

    The Python language created in 1991 by Guido Van Rossum.
    Aiming at productivity and readability.
'''
print('Estou aprendendo Python!!!')
print(" # Concatenando(unindo) duas Strings(texto e/ou caracteres) em python:")
nome = 'Flávio'
nome_do_meio = ' de Medeiros'
ultimo_nome = 'Lima'
idade = 46
altura = 1.77
resultado = nome + ultimo_nome

print('Soma de 7 + 4 é:', 7 + 4) # saída: 11, apresenta a soma dos valores.
print('Unindo dois valores 10 + 10 -> ' + '10' + '10') # saída: 1010, apresenta a junção(comcatenação) dos valores.

print(nome + nome_do_meio + ultimo_nome) # saída: Fláviode MedeirosLima, sem separação.
print(" ")
print(nome, nome_do_meio, ultimo_nome) # saída: Flávio de Medeiros Lima, com separação.
print(" ")
print(nome, idade, altura)
print(" ")
print(resultado)
''' print('Olá' + 5)' saída:  Dá erro -> Traceback (most recent call last):
File "/home/tads/Learning_Programming_Languages/intellij-projects/codes-python-intellij/initial.py", line 21, in <module>
print('Olá' + 5)
TypeError: can only concatenate str (not "int") to str '''
print('Olá,', 5)
print('Olá,', 5)
print('=======================================================================')