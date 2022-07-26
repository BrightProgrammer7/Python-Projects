no_list = [5,20,12,6]

def maximum(no_list):
    max = 0
    for num in no_list:
        if max < num:
            max = num
    return max
print(maximum(no_list))