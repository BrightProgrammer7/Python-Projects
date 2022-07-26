def find_512(x, y):
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                return f"{x} * {y} == 512"
    print(f"{x} * {y} == 512")    

x = 0
y = 0
find_512(x, y)                
