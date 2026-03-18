'''Crie um programa python que peça a idade de um pessoa e verifique se ele tem 
idade para se alistar nas forças armadas'''

idade = int(input('Informe a sua idade: '))

if idade >= 18:
    print('Alistamento obrigatório.')
else:
    print('Não tem idade para o alistamento.')