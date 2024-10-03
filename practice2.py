def string_clean(text):
    #removes all non-string keys from input
    result = ""
    for character in (text):
        if character.isalpha():
            result = result + character.lower()
    return result
    

characters = (input("Enter your string:"))

output = string_clean(characters)
print(output)