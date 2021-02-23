from random import randint

t = ["Rock", "Paper", "Scissors"]

# assign aa random play to computer
computer = t[randint(0, 2)]

# set player to false
player = False

while player == False:
    player = input()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose !", computer, "covers", player)
        else:
            print("You Win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose !", computer, "cut", player)
        else:
            print("You Win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose.... !", computer, "smashes", player)
        else:
            print("You Win!", player, "cut", computer)

    else:
        print("That's not a valid play.Check your spelling!")

    player = False
    computer = t[randint(0, 2)]
