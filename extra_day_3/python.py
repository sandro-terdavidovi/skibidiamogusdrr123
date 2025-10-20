temperatures = [15, 22, 30, 18, 9]

for i in temperatures:
    print(i)
    if i > 20:
        print("warm day")
    else:
        print("cold day")
        

score = int(input())
has_pass = input()

if score >= 50 and has_pass == "yes":
    print("you passed")
elif score < 50 and has_pass == "yes":
    print("low score but passed")
else:
    print("you failed")


data = "a"

if data == float:
    print("float type found")
elif data == bool:
    print("boolean type found")
else:
    print("different data type found")
    
    
secret_number = 7

choice = int(input("type number from 1 to 10"))


if choice > secret_number:
    print("too high")
elif choice < secret_number:
    print("too low")
else:
    print("you won!")


grades = [85, 60, 45, 90, 72]

for i in grades:
    if i >= 80:
        print("excellent")
    elif grades > 50 and grades < 80:
        print("good")
    else:
        print("needs impovement")