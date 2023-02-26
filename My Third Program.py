import random


array = []
sum = 0

for x in range(10):
    array.append(random.randint(1, 100))

for y in array:
    sum = sum + y

smallest = array[0]

for x in range(len(array)):
    if array[x] < smallest:
        smallest = array[x]

highest = array[0]

for x in range(len(array)):
    if array[x] > highest:
        highest = array[x]
print(array)
print(sum)
print(f'Smallest : {smallest} Highest : {highest}')
