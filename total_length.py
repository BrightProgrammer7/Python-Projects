def total_length(list):
    total = 0
    for string in list:
        total = total + len(string)
    return total

list = input("list of strings: ")    
total_length(list)