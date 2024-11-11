time = (input())
num_of_tasks = (input())
time = int(time)
num_of_tasks = int(num_of_tasks)
time_used = 0
counter = 0
tasks = []

for i in range (num_of_tasks):
    num_add = (input())
    num_add = int(num_add)
    tasks.append(num_add)
tasks.sort()
print(tasks)

while (True):
    if (time >= time_used): 
       time_used + 1
    else:
        break 

print(counter)