
word = "My Name is bob"
lenght = len(word)

# # print(word)
# #
# # for j in word:
# #     print(j)
#
# # Task:  Remove the gaps from a string
# word = word.replace(" ","")     # Replace Command
# # print(word)
# # no_space = word.split(" ")
# # ans = ""
# # for i in no_space:
# #     ans = ans + i
# #
# # print(ans)
# find = "My"
# # if word.find(find) >= 0:
# #     print(find," is found")
# # else:
# #     print("Not found")
# print(word.strip('My'))    # It will work for the first value or the last one.



file = open('words.txt')
count = 0
for i in file:
    # if i.find('abc') >= 0:
    #     pass
    # else:
    #     print(i)
    #     count += 1
    if len(i) > 10:
        print(i)

print("Total Words: ",count)