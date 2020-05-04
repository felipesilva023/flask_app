def print_vowels(phrase: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    found = []
    for letter in phrase:
        if letter in vowels:
            if letter not in found:
                found.append(letter)
    return found
