import random
print("The computer has the guess the user's number. User must enter 'Yes' if guess is correct or give indication like 'Too high' or 'Too low'")
x = int(input("Enter upper limit of the range: "))
guess = random.randint(1,x)
x_min = 1
x_max = x
print(f"Guess: {guess}")
ans = input()
ans_lower = ans.lower()
while ans_lower != "yes":
    # if guess > x_max:
    #     print("Invalid input.")
    # elif guess < x_min:
    #     print("Invalid input.")
    
    if ans_lower == 'too high':
        x_max = guess
        guess = random.randint(x_min, guess)
        
    elif ans_lower == 'too low':
        x_min = guess
        guess = random.randint(guess, x_max)
        
    print(f"Guess: {guess}")
    ans = input()
    ans_lower = ans.lower()

if ans_lower == 'yes':
    print("Thank you. ")

    
