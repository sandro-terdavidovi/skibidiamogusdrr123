hi = "hello"

if hi[::1] == "hello":   
    print("hi")
else:
    print("thats not hi bye :( (sadly)")      
             
li = ["hi0", "hi1", "hi2", "hi3"]

for i in li[::-2]:
    print(i)   
    
ez = input("type your word and i will reverse it")
print(ez[::-1])

xd = "omegaliminalsubmanufacturereversing"

print(xd[0:6])
print(xd[-4:])
print(xd[16:26])
print(xd[::-1])
print(xd[::2])