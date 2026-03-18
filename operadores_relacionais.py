# expressao logica ou expressão booleana
# = --> UM sinal de igual, operador de ATRIBUIÇÃO
#== --> DOIS sinais de igual, operador de COMPARAÇÃO

x = 10
y = 3 

print(x > y)    #Maior que              #True
print(x >= y)   #Maior ou igual que     #True
print(x < y)    #Menor que              #False
print(x <= y)   #Menor ou igual que     #False
print(x == y)   #Igual que              #False
print(x != y)   #Diferente que          #True

#Operadores logicos
#and [&&] ==> retornar True, todas as condições 
#             tem que ser VERDADE (TRUE).

#or  [||] ==> retornar True, se pelo menos uma condição 
#             for VERDADE (TRUE).

#not [ !] ==> inverte a expressão lógica, 
#             se for True passa a ser False, 
#             se for False passa a ser True.

a = 5
b = 7
c = 10

print()
print(a + b > c or c-a > b)
print(b * a == 35 and c + 2 == a + b)
print(a > 0 and b < 10 and c + a == 15)
print(not False or not True)
print(a * 2 > 12 and b + c < 10 or a > 3)

