import random
n = random.randint(1,100)
a = -1
guesses = 0

while(a != n):
    a = int(input("Guess a number :"))
    if(a > n):
        print("Lower number please")
        guesses +=1
    else:
        print("Higher number please")
        guesses +=1

print(f"You have guesssed the number {n} correctly in {guesses} attempt ")

