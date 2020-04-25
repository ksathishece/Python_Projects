import random

mypassword = "Yeshwant24"

print("Please type in your password for access ?")

password = input()

if (password == ""):
    print("empty password")
elif(mypassword == password):
    print("access granted")
else:
    print("wrong password")


sum = 0
for i in range(101):
    sum = sum + i

print("the value of i " + str(sum))

for i in range(6, -6, -1):
    print("the value if i = " + str(i))



for j in range(7):
    print(random.randint(120,999))



