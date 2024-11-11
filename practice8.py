def mean_checker(nums):
    return sum(nums) / len(nums)
    

def median_checker(nums): 
    sorted_list = sorted(nums)
    middlenum = len(sorted_list) / 2
    if len(sorted_list) % 2 == 0:
        return sorted_list[middlenum]
    else :
        return sorted_list[middlenum]

list1 = [1, 2, 3, 3, 4, 5]
output = median_checker(list1)
print(output)