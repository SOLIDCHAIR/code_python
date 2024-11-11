def pattern_creator(number):
    result = ""
    next_character = "1"
    for i in range(1, number+1):
        if (next_character == "1"):
            result = result + next_character
            next_character = "0"
        else:
            result = result + next_character
            next_character = "1"
    return (result)

userin = int(input("Enter your number:"))
output = pattern_creator(userin)
print(output)
    

        