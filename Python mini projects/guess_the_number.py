import random

def func(x):
    no = random.randint(1,x)
    guess = int(input("Guess the random number:")) #initial value
    while True:
        if(guess > no):
            print("Oops. You guessed a larger number \n Try again:")
            guess = int(input())
        elif(guess < no):
            print("Oops. You guessed a smaller number \n Try again:")
            guess = int(input())
        elif(guess == no):
            print("Correct guess. Congratulations!")
            break

x = int(input("Enter upper limit of range"))
if(x==0):
    print("Wrong input. Enter a no. greater than 1")
    x = int(input())
else:
    func(x)
        


