import random
opt = ["rock", "paper", "scissor"]

running = True

while running:
    player = None
    while player not in opt:
        player = (input("Enter your choice (rock, paper, scissor): ")).strip().lower()

    computer = random.choice(opt)

    print("Player choice: " + player)
    print("Computer choice: " + computer)


    if player==computer:
        print("It's a tie.")

    elif player=="rock" and computer=="scissor":
        print("Player wins.")

    elif player=="paper" and computer=="rock":
        print("Player wins.")

    elif player=="scissor" and computer=="paper":
        print("Player wins.")

    else:
        print("Computer wins.")
    
    que = input("Play again y/n : ").strip().lower()

    if que!="y":
        running=False




    