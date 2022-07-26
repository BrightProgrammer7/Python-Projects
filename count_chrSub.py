def count_character(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1   
    print(total)
count_character("papa pony and the parcel post problem", "p")

def count_substring(string, sub):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            total += 1
            index += len(sub)
        else:
            index += 1
    print(total)        

count_substring('love, love, love, all you need is love', 'love')    
count_substring('AAAA', 'AA')