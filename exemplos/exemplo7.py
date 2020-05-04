from random import randint

list1 = []

for num in range(6):
    var_random = randint(1, 10)
    print('')
    print('Adicionando item a list1...')
    list1.append(var_random)
    print(f'item {var_random} adicionado com sucesso!')

print('')
print(list1)
