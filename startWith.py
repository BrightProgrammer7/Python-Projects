def start_A(s):
    return s.startswith("A")

def start_K(s):
    if s[0] == "K":
        return True
    else:
        return False
        
print(start_K("Kelly"))
print(start_K("Abe"))

word = input("Possible tag: ")
def possible_tag(word):
    if word.startswith("<") and word.endswith(">"):
        print(word, "could maybe be an HTML tag")
    else:
        print(word, """is definitely not an HTML tag\
        (but might contain one)""")
possible_tag(word)        