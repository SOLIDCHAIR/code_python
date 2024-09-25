f_name = input("Enter your first name ")
l_name = input("Enter your last name ")
year = int(input("enter your birth date "))
age = 2024 - year 
print("Hello", f_name, l_name)
print("you are ", age, " years old")
if age < 19:
    print("you are not old enough to drink")
else: 
    print("you are old enough to drink")