

array = [1, 2, 3, 4, 5]


def Array():
    for x in range(len(array)):
        number = int(input("Enter a number : "))
        array.append(number)
    print(array)



Array()
