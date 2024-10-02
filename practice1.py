def factor_count(number):
    counter = 0
    for divider in range(1, number+1):
        if number % divider == 0:
            counter += 1 
    return counter
         

limit = int(input("Enter a number: "))

for num in range(1, limit+1):
    factor_size = factor_count(num)
print(f"{num} has {factor_size} factors.")