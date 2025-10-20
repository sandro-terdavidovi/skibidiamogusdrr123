numbers = [2, 5, 8, 11, 14]

for i in numbers:
    if i % 2 == 0:
        print("even number")
    else:
        print("odd number")


age = int(input("type your age"))

id = input("do you have id y/n")

if age >= 18 and id == "y":
    print("allowed to enter")
elif age < 18 and id == "y":
    print("too young but have id")
else:
    print("not allowed")
    
var = input("type your thing")

if type(var) == str:
    print("string")
elif type(var) == int:
    print("integer")
else:
    print("else")


number = 5

idk = int(input("type your number"))

if idk == number:
    print("you won!")
elif idk > number:
    print("too high")
else:
    print("you lose!")
    
