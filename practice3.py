def palindrone_check(text):
    return text == text [::-1]


#get user input, do the program, give output
user_in = (input("Enter a word"))
output = palindrone_check(user_in)
if output == True:
    print("it a palindrone")
else:
    print("it is not a palindrone")