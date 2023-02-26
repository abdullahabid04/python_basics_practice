file = open('Lectures/words.txt')
allowed = input('Enter a string to search relavent Letters')
def uses_all(letter,required):
    for word in required:
        if word not in letter:
            return False
    return True
count = 0
for lines in file:
    ans = uses_all(lines,allowed)
    if ans:
        print(lines)
        count += 1
print("Total: ",count)