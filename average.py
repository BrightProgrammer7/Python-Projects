no_list = [10, 20, 30, 40]

def average(x):
    sum = 0
    for num in x:
        sum += num
    return sum / len(x)   
       
print(average(no_list))