'''Verificar se um valor inteiro e par ou impar'''
numero = int(input('Informe um valor: '))
#No python a identação é OBRIGATORIA
#Os comandos IF e ELSE sempre terminam com :
#E a proxima linha deve ser identada.
if numero % 2 == 0:
    print('Valor PAR!')
    print('Final da verificação do IF [par]')
else:
    print('Valor IMPAR!')
    print('Final da verificação do ELSE [impar]')
print('Final do programa')