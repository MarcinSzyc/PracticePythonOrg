import random

a = random.sample(range(100), 5)
b = random.sample(range(100), 7)

c = sorted(set(a+b),key=int)
print(a)
print(b)
print(c)
