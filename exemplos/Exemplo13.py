vowels = ['a', 'e', 'i', 'o', 'u']
found = {}

var = 'calendario'

for letter in var:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for key, value in sorted(found.items()):
    print(f'{key} = foi encontrada {value} vez(es)')
