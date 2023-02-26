file = open('Lectures/words.txt')
for line in file:
    if len(line) > 20:
       print(line)

