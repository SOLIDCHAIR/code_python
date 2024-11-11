def string_compare(word1, word2):
    output_list = []
    set_word2 = set(word2)
    set_word1 = set(word1)
    for character in set_word1:
        if character in set_word2:
            output_list.append(character)
    return (output_list)

userin1 = (input("Enter your word:"))
userin2 = (input("Enter your second word:"))
output = string_compare(userin1, userin2)
print(output)