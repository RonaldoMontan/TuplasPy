classificacao = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG', 'Santos', 'Flamengo', 'Fluminense', 'Botafogo', 'São Paulo', 'Bragantino', 'Avaí', 'Atlético-GO', 'Ceará', 'Coritiba', 'América-MG', 'Goiás', 'Cuiabá', 'Fortaleza', 'Juventude')

print(classificacao[:5])#primeiros
print('\n')
print(classificacao[-4:])#ultimos
print('\n')
print(sorted(classificacao))#ordem alfabetica
print('\n')
times = str(input("Qual time você que saber? "))
if classificacao.index(times) != True:
    print(classificacao.index(times)+1)

else:
    print('Time não encontrado...')    