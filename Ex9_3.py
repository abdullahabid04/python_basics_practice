file = open('Lectures/words.txt')
forbidden = input('Enter a string of Forbidden Letters')
def avoids(letter,forbidden):
    for word in letter:
        if word in forbidden:
            return False
    return True
for lines in file:
    ans = avoids(lines,forbidden)
    if ans:
        print(lines)

# boolean Variables (True, False)