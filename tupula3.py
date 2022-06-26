from random import randint
from time import sleep

print('Vou sortear 5 numeros...')
sleep(2)
sortido = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(sortido)
sleep(1)
print(f'o menor valor foi {sorted(sortido)[0]}')
print(f'o maior valor foi {sorted(sortido)[4]}')

#ou pode fazer assim
#print(f'o maior valor foi {max(sortido)}')
#print(f'O menor valor foi {min(sortido)}')