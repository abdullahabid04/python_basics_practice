file = open('Lectures/words.txt')
global has_e
has_e = 0
total = 0
def has_no_e(line):
    global has_e
    if line.find('e'):
        has_e += 1
        return True
    else:
        return False
for line in file:
    total+=1
    ans = has_no_e(line)
    if ans:
        print(line)
print("Percentile of e: ",(has_e * 100)/total,"%")


