def anagram_checker(word1, word2):
    list1 = list(word1)
    print (list1)
    list2 = list(word2)
    print (list2)
    sorted_list1 = sorted(list1)
    print (sorted_list1)
    sorted_list2 = sorted(list2)
    print (sorted_list2)
    if sorted_list1 == sorted_list2: 
        return (True)
    else: 
        return (False)

userin1 = (input("Enter your word:"))
userin2 = (input("Enter your second word:"))
output = anagram_checker(userin1, userin2)
print(output)
     
