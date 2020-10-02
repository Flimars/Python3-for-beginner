# 5. Desenvolva o algoritmo para converter uma temperatura em graus Fahrenheit para
# graus Celsius.
# A fórmula para conversão é a seguinte: C/5 = F - 32/9
# Onde:C = temperatura em graus Celsius, F = temperatura em graus Fahrenheit.

f = int(input('Digite a temperatura em Fahrenheit:'))
c = 5 * (f -32)/9
print('A temperatura {} F corresponde a {} °C'.format(f,c))

