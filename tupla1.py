tupula = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continua = ''

while continua in 'sS':    
    while True:
        escolha = int(input('Digete um valor entre 0 - 20:  '))
        if escolha <= 0 or escolha <= 20:
            break
        print('tente novamnet...', end='')

    print(tupula[escolha])
    continua = str(input('Gostaria de continuar? '))[0]

print('Programa encerrado')