import random

# 
rock = "RRRRRRRR"
paper = "PPPPPPPP"
scissor = "SSSSSSSS"
# 
images = [rock, paper, scissor]
# 
user_choice = int(input("what do you wannna choose? 0 for rock, 1 for paper and 2 for scissor\n"))
# so as not to parse a value out of range of game images index
if user_choice >= 3:
    print("you entered an invalid character please try again")
else:
    print(images[user_choice])
    computers_choice = random.randint(0, 2)
    print("The computer chose"),
    print(images[computers_choice])
    # 
    if user_choice == computers_choice:
        print("you draw")

    elif computers_choice > user_choice:
        print("you lose")
    elif user_choice > computers_choice:
        print("you win")
    elif user_choice == 0 and computers_choice == 2:
        print("you win")
    elif computers_choice == 0 and user_choice == 0:
        print("you lose")
