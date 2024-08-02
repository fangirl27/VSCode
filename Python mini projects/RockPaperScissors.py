import random
print("Rock Paper Scissors game: User v/s Computer. Enter r, p or s")

user = input()
if (user != 'r' and user != 'p' and user != 's'):
    print("FUck off tanish")
    quit()
comp_int = random.randint(1,3)
comp = '0'
print(comp_int)
if comp_int == 1:
    comp = 'r'
elif comp_int == 2:
    comp = 'p'
elif comp_int == 3:
    comp = 's'

print(f"Computer response: {comp}")
if (user == 'r' and comp == 'r') or (user == 'p' and comp == 'p') or (user == 's' and comp == 's'):
    print("Tie. ")
elif (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p'):
    print("User wins")
elif (user == 'r' and comp == 'p') or (user == 'p' and comp == 's') or (user == 's' and comp == 'r'):
    print("Computer wins")