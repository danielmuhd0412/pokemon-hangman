"""
Implementation of hangman.
The program reads in the attached list of words (file words.txt) and selects a random word with at least five characters.
The user attempts to guess the word by entering one character at a time. 
The user is allowed a fixed number of failed attempts.

The game takes place in the following loop:
– The program prints the guesses so far, shows the guessed characters (the ones not yet guessed are replaced with ’*’s), and prompts the user for a guess.
– The user enters the guess. If this is not an alphabetical string of length one, or if it has already been tried, the program prompts the user again.
– The user is informed whether the guess was correct or not. If all the characters have been guessed, the answer is revealed and the game stops. 
- If the attempt was not correct and there are no more attempts left, the game user has lost and the game is over. Otherwise, the loop is repeated.
"""
import random as r

def hangman(max_tries=5, word=None):
    
    # grabs random word from words.txt if word = None
    if word == None:
        with open('words.txt', 'r') as file:
            words = [word for word in file]
        word = words[r.randint(0, len(words)-1)].strip()
        
    guesses = []
    current = len(word) * '*'
    
    # main loop
    while True:
        print(f"\nGuesses so far: {guesses}")
        print(f"Current status: {current}")
        
        # gets input from user and checks its validity
        done = False
        while not done:
            guess = input(f'Enter a character: ')
            if guess in guesses:
                 print("You already tried that!\n")               
            elif len(guess) == 1 & guess.isalpha():
                done = True
            else:
                print('Only alphabetical characters, please!\n')    
        
        guesses.append(guess)
        
        if guess in word: # guess is correct
            print(f"{guess} is in the word!")
            
            # updates current status
            indexes = [i for (i, ss) in enumerate(word) if ss is guess]
            for index in indexes:
                current = current[:index] + guess + current[index+1:]
        else: # guess is wrong
            max_tries -= 1

            if max_tries == -1:
                print(f"\n{guess} is not in the word... you lost!")
                print(f"The word was {word}")
                break
            else:
                print(f"{guess} is not in the word... try again!")

            if max_tries > 1:
                print(f"You can only make {max_tries} more mistakes!")
            elif max_tries == 1:
                print(f"You can only make one more mistake!")
            elif max_tries == 0:
                print(f"You can no longer make any mistakes!")
        
        if current == word: # user guessed word correctly within number of tries
            print(f"\nThe word is {word}")
            print(f"You've guessed it!")
            break
            
if __name__ == '__main__':
    # hangman(word='police')
    hangman()