# 7. Construa um algoritmo que dadas as entradas: distância do trajeto e velocidade
# média da viagem, informe o tempo que uma família levará saindo de sua cidade de
# férias até o destino previsto. Após o cálculo, o algoritmo deve mostrar o tempo
# calculado.

distancia = float(input('Digite a distância percorrida: '))
velocidade = float(input('Digite a velocidade média: '))
tempo = (distancia/ velocidade) * 60
print('O tempo da viagem = ', tempo, ' minutos')