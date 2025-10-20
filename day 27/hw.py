hi = "hi"
hi2 = 2
hi3 = True
hi4 = 3.14

print(type(hi), hi)
print(type(hi2), hi2)
print(type(hi3), hi3)
print(type(hi4), hi4)

hello1 = int(input("how much brothers and sisters you have"))
hello2 = int(input("what age you are"))
hello3 = input("what is your name")


print(type(hello1), hello1)
print(type(hello2), hello2)
print(type(hello3))

hi5 = list(range(3, 30))

for i in hi5:
    if i % 3 == 0:
        print("yes", type(i))
    else:
        print("no", type(i))
