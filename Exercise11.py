def get_number(text):
    return int(input(text))

num = get_number('Please provide your number here: ')    
l = []
for i in range(1,num+1):
    if num % i == 0:
        l.append(i)
    
print(l)
if len(l) >2:
    print('{} is not a prime'.format(num))
else:
    print('{} is  a prime'. format(num))
