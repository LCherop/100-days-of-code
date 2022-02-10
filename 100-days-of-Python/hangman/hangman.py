import random
from turtle import clear
import hangman_art
import hangman_words

print(hangman_art.logo)
lives = len(hangman_art.stages) -1
end_of_game = False


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

display = []
for letter in chosen_word:
  display.append("_")


while end_of_game == False:
    letterd = input("Guess a letter: ").lower()
    
    clear()
    if letterd in display:
        print(f"You've already guessed {letterd}")

    for i in range(word_length):
        if(letterd == chosen_word[i]):
            display[i] = letterd
    print(f"{' '.join(display)}") 
    
    if not letterd in display:
        print(f"You guessed {letterd}, that's not in the word. You lose a life.")
        lives -=1
        if lives == 0:
            end_of_game = True
            print(hangman_art.you_lose)
            
                 
    
    if "_" not in display:
        end_of_game = True
        print(hangman_art.you_win)
    
    print(hangman_art.stages[lives])
    