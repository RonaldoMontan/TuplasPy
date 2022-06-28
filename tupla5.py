palavra = ('Cerveja', 'Lupulo', 'Agua', 'Malte', 'Levedura', 'Cevada', 'Grao')

for j in range(0, len(palavra)):
    provisorio_palavra = palavra[j]
    print(f'\n{palavra[j].upper()} tem as seguintes vogais:', end=' ')

    for i in range(0, len(provisorio_palavra)):        
        if provisorio_palavra[i] == 'a' or provisorio_palavra[i] == 'e' or provisorio_palavra[i] == 'i' or provisorio_palavra[i] == 'o' or provisorio_palavra[i] == 'u':
           vogais = provisorio_palavra[i]
           print(vogais, end=' ')   
           
#outra manira de se fazer, bem mais fácil 

for p in palavra:#analisa cada elemento da tupla
    print(f'\n{p.upper()} tem as seguintes vogais: ', end='')

    for letra in p:
        #agora analisando o primeiro elemento, virou outra tupla ex ('c','e','r','v','e','j','a') com isso podemos navegar em suas posções
        if letra.lower() in 'aeiou':
            print(letra, end=' ')   
