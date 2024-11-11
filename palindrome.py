userin = (input("Enter your number:"))
userlist = list(userin)
print (userlist)
reverselist = userlist[::-1]
print (reverselist)
if userlist == reverselist: 
    print("cool")
else :
    print("not cool")