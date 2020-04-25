import random

# get a secret number
secretnumber = random.randint(1,10)

print("guess a number between 1 and 10 ")

for retries in range(7, -1, -1):
    myguess = int(input())

    if(myguess == secretnumber):
        print("Great, thats right, the number is " + str(myguess))
        break
    else:
        print("sorry try again, retries left = " + str(retries))
        continue

print("the secret number is = " + str(secretnumber) + " retries left = " + str (retries))
