#get names as strings
f_name = input("Enter your first name ")
l_name = input("Enter your last name ")
#get year an int 
year = int(input("enter your birth date "))
#convert the year into age 
age = 2024 - year 
#print the information we know
print("Hello", f_name, l_name)
print("you are ", age, " years old")
#calculate if the are old enough to drink
if age < 19:
    print("you are not old enough to drink")
else: 
    print("you are old enough to drink")