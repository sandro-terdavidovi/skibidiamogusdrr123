i = 100

while i != 20:
    print(i)
    i = i * 2
    
    
hi = input("type your password")

password = "1231123"

while hi != password:
    print("wrong password")
    hi = input("type your password")
print("correct password")

for i in range(0, 200, 10):
    print(i)
    
list = ["hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi",]
list[8] = 100
list[9] = 100
list[12] = 100
list[14] = 100
print(list[0:14])


input1 = int(input("type your number"))
op = input("operator")
input2 = int(input("type your number"))

ops = ["+", "-", "*", "/"]

if op not in ops:
    print("invalid")
else:
    if input1 == str or input2 == str:
        print("invalid character")
    else:
        if op == "+":
            print(input1 + input2)
        elif op == "-":
            print(input1 - input2)
        elif op == "*":
            print(input1 * input2)
        elif op == "/":
            print(input1 / input2)