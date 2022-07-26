def locate_first(string, sub): 
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            return index
        else:
            index += 1  
    return -1

print(locate_first('cookbook', 'ook'))
print(locate_first('all your bass are belong to us', 'base'))

def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    print(matches)
locate_all('cookbook', 'ook')    