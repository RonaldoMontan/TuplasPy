tupla = (int(input("Valor 1: ")),
         int(input("Valor 2: ")),
         int(input("Valor 3: ")),
         int(input("Valor 4: ")))


print(tupla)
print(f'Quantidade 9 foi {tupla.count(9)}')
if 3 in tupla:
    print(f'Posição do primeiro 3 é {tupla.index(3)+1}')
else:
    print('Valor 3 não foi encontrado')    

for posição in range(len(tupla)):
    if tupla[posição]%2 == 0:
        print(f'Valores pares encontrado foi {tupla[posição]}')