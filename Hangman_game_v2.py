# Hangman game alternative version 

# Import
import random
from os import system, name

# clear screen
def clear_screen():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Function to draw hangman
def display_hangman(chances):

    # Stages
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

# Game function
def game():
    clear_screen()
    print("\nWelcome to Hangman Game!")
    print("Guess the word below, it's a continent!\n")
    
    words = ['africa', 'antarctica', 'america', 'asia', 'europe', 'oceania']
    
    word = random.choice(words)
    
    discovered_letters = ['_' for _ in word]
    
    chances = 6
    
    wrong_letters = []
    
    letter_tried = []  # Initialize letter_tried list
    
    while chances > 0:
        print(display_hangman(chances))
        print("Word:", ' '.join(discovered_letters))  # Use discovered_letters instead of board
        print("\n")
        
        attempt = input("\nType a letter: ").lower()
        
        if attempt in letter_tried:
            print("You already tried this letter. Choose another please.")
            continue
        
        letter_tried.append(attempt)
        
        if attempt in word:
            print("You got the letter right!")
            for index in range(len(word)):
                if word[index] == attempt:
                    discovered_letters[index] = attempt
            
            if "_" not in discovered_letters:
                print("\nCongrats! You won! The word was: {}".format(word))
                break
        else:
            print("That letter is not in the word...")
            chances -= 1
    
    if "_" in discovered_letters:
        print("\nYou lost... The word was: {}.".format(word))

if __name__ == "__main__":
    game()
    print("\nCongratulations, you're learning continents names :D\n")
