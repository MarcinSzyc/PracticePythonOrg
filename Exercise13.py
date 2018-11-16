def how_many(text='How many Fibonacci numbers to generate? '):
    return int(input(text))
    
num = how_many()
if num == 1:
    l = [1]
    print(l)
elif num == 2:
    l = [1,1]
    print(l)
else:
    l = [1,1]
    for i in range(num):
        if i == 1 or i == 2:
            continue
        else:
            l.append(l[i-2]+l[i-1])
    print(l)
