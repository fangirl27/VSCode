import random
from word_for_hangman import words
#choosing random word from dataset
w = random.choice(words)
print("Hangman dead after 6 incorrect tries. To give up, type 'Give Up' ")
c = 6 #six guess tries

def valid_word(w):
    while '-' in w or ' ' in w or '.' in w:
        w = random.choice(words)
    return w.lower()

def guess(w, wg, counter):
    g = input("Guess a letter:")
    #while counter >= 1:
    if g.lower() == 'give up':
        print(f'The word is: {w}')
        quit()
    else:
        c2 = 0
        for i in range(0, len(w)):
            if w[i] == g:
                wg[i] = g 
            else:
                c2 += 1
        print(wg)
        if c2 == len(w):
            counter = counter - 1
            print("Wrong guess.")
    return counter
        

word = valid_word(w)
n = len(word)
wg = ['_' for i in range(1, n+1)]

print(f"The word has {n} letters")

while '_' in wg and c >= 1:
    c = guess(word, wg, c)
if (c==0):
    print(f"Oops. Hangman dead. Correct word was {w}")
