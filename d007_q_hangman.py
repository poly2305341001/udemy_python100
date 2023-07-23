import random
import d007_q_module

# stages = ["complete", "one_leg", "two_arms", "one arm", "body", "head"]
# word_list = ["aardvark", "baboon", "camel"]
from d007_q_module import word_list, stages

chosen_index = random.randint(0,len(word_list)-1)
chosen_word = word_list[chosen_index]
# chosen_word = random.choice(word_list)

lives = 6

print(d007_q_module.logo)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")
    # display += "_"

while display != list(chosen_word) and lives != 0:
    print(f"{' '.join(display)}")

# end_of_game = False
# while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # for letter in chosen_word:
    #     if letter == guess:
    #         print("Right")
    #     else:
    #         print("Wrong")

    if guess in display:
            print(f"You've checked {guess} already :)")
    elif guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"You checked {guess}. But you missed a life :(")
        if lives == 0:
            print("You lose.")
        continue
    else:
        for idx in range(len(chosen_word)):
            if chosen_word[idx] == guess:
                display[idx] = guess
        
    # display_copy = []
    # display_copy.extend(display)    

    # i = 0
    # for letter in chosen_word:
    #     if letter == guess:
    #         display[i] = guess
    #     i += 1
    
    # if display == display_copy:
    #     lives -= 1
    #     print(stages[lives])
    #     if lives == 0:
    #         print("You lose.")
    #     continue

    if display == list(chosen_word):
        print("You win.")

    # if "_" not in display:
    #     end_of_game = True
    #     print("You win.")