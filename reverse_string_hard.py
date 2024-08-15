def reverse_word(word):
    reversed_word = ""
    index = len(word) - 1

    while index >= 0:
        reversed_word += word[index]
        index -= 1

    return reversed_word

word = "Python"
reversed_word = reverse_word(word)
print(f"A palavra invertida é '{reversed_word}'")
