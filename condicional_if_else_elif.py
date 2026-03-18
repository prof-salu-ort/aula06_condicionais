'''Criar um programa python para verificar se uma pessoa pode votar'''
# 16 e 17 VOTO OPCIONAL
# > 65    VOTO OPCIONAL
# > 18     VOTO OBRIGATORIO
# < 16    AINDA NÃO PODE VOTAR

idade = int(input('Informe a sua idade: '))

if(idade == 16 or idade == 17 or idade > 65):
    print('Voto opcional')
elif idade >= 18 and idade <= 65:
    print('Voto obrigatorio')
elif idade >= 0 and idade < 16:
    print('Não pode votar')
else:
    print('Idade invalida')