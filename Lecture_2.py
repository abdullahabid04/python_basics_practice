# input from user

#1) Take Input: name, age, school name
# 2) show output
# questions = ["What is your name","How old are you?","What is your school name?"]
# answers = ["My name is:","I am %s years old","My school name is:"]
# save_values = []   # empty list
# for a in range(3):
#     z = input(questions[a])
#     if a == 1:
#        print(answers[1].format(z))
#     else:
#        print(answers[a],z)
#     save_values.append(z)
# print(save_values)
# print("Your name is:",a,"\n","Your age is:",b,"\n","Your school name is:",c)

# Functions

def Sum(first,second):
    Add = first + second
    return Add

# local variable
# global variable    || Every thing outside the functions is in the main program

a = input("enter a value a")
b = input("enter a value b")
a = int(a)   # global variable
b = int(b)
ans = input("enter your required operations (sum,multiply,minus)")
if ans == "sum":
    add = Sum(a,b)
    print(add)
elif ans == "multiply":
    mult = a * b
    print(mult)
elif ans == "minum":
    minus = a - b
    print(minus)
else:
    print("you entered wronge operation")