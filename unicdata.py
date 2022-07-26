import unicodedata

chr = input("Enter your character: ")

def anime():
    print(chr, ":", unicodedata.lookup(chr))

anime()

 
      