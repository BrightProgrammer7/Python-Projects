no_list = [22,22,2,1,11,11,2,2,3,3,3,4,5,5,5,55,55,66]

def unique_list(l):
    l = []
    for num in no_list:  
        while num not in l:
            l.append(num)
    return l
        
print(unique_list(no_list))