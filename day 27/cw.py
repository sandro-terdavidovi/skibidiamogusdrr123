intxd = 5
strxd = "hi"
boolxd = True
floatxd = 1.0

print(intxd, type(intxd))
print(strxd, type(strxd))
print(boolxd, type(boolxd))
print(floatxd, type(floatxd))

#bonus:
user = input("hi")
print(user, type(user))

user1 = input("type your age")
user2 = input("type your fav num")
user3 = input("type your name")

print(user1, type(user1))
print(user2, type(user2))
print(user3, type(user3))

float(user2)
float(user1)


li = list(range(5, 100))

for i in li:
    if i % 2 == 0:
        print("even number")
    else:
        print("odd number")

# ფუნქციები გამოიყენება რო რააცა ელემნტს რააცა გაუკეთო მაგალითად პრინტ() ეს ფუნქცია წერს ტერმინალში ტექსტი
# type() print() int() str() boolean() float() range()

# არი რაც ფუნქციის () არი