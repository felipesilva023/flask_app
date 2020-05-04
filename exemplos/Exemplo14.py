vowels = ['a', 'e', 'i', 'o', 'u']
found = []

var = 'paralelepipido'

for letter in var:
    if letter in vowels:
        found.append(letter)

updated_list = set(found)

print(updated_list)
