def constant_checker(word):
    lower_word = word.lower()
    counter = 0
    for character in (lower_word):
        if character.isalpha() and character not in ("a", "e", "i", "o", "u"):
            counter = counter + 1
    return (counter)
    
characters = (input("Enter your string:"))

output = constant_checker(characters)
print(output)
