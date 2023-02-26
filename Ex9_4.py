file = open('Lectures/words.txt')
allowed = input('Enter a string to search relavent Letters')
def uses_only(letter,allowed):
    for word in letter:
        if word not in allowed:
            return False
    return True
for lines in file:
    ans = uses_only(lines,allowed)
    if ans:
        print(lines)