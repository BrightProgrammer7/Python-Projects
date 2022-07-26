def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            print("True")
        index += 1
        print("False")

string = 'waffles'
substring = 'ff'
is_substring(substring, string)