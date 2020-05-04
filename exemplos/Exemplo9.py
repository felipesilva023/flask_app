vowels = ['a', 'e', 'i', 'o', 'u']
found = []

var = 'mouse'

for letter in var:
    if letter in vowels:
        found.append(letter)

for l in found:
    print(l)
