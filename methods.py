words = ["echidna", "dingo", "crocodile", "bunyip"]
words.append("platypus")
words.extend("abc")
words.extend(["kangaroo", "wallaby"])
print(words)
words.reverse()
print(words)
words.sort()
print(words)

first_list = [1, 2, 3]
second_list = [4, 5, 6]
for item in second_list:
    first_list.append(item)
first_list.extend([7, 8, 9])
print(first_list)