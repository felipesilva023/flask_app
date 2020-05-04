# coding: utf-8

from random import randint
from time import sleep

print('Máquina: vou pensar em um número e você precisa adivinhar')

num_random = randint(1, 10)

sleep(2)

print('Ok, tente adivinhar:')

our_guess = int(input('Digite seu palpite: '))

# Comparar resultados:

if our_guess == num_random:
    print('Uau, você acertou.')
else:
    print('Não foi dessa vez.')
