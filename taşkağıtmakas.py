import random 
options = "rock","scissors","paper"
raund = int(input("How many raunds do you want to play: "))
player_1 = "Ahmet"
player_2 = "Eren"
p1point = 0
p2point = 0
for i in range(1,raund+1,1):
    player1 = options[random.randint(0,2)]
    player2 = options[random.randint(0,2)]
    if player1 == "rock" and player2 == "scissors":
        print(player_1,":",player1)
        print(player_2,":",player2)
        p1point += 1
        print(player_1,"win ")
    elif player1 == "rock" and player2 == "paper":
        print(player_1,":",player1)
        print(player_2,":",player2)
        p2point += 1
        print(player_2,"win")
    elif player1 == "paper" and player2 == "rock":
        print(player_1,":",player1)
        print(player_2,":",player2)
        p1point += 1
        print(player_1,"win")
    elif player1 == "paper" and player2 == "scissors":
        print(player_1,":",player1)
        print(player_2,":",player2) 
        p2point += 1
        print(player_2,"win")
    elif player1 == "scassers" and player2 == "paper":
        print(player_1,":",player1)
        print(player_2,":",player2)
        p1point += 1
        print(player_1,"win")
    elif player1 == "scissors" and player2 == "rock":
        print(player_1,":",player1)
        print(player_2,":",player2)
        p2point += 1
        print(player_2,"win")
    elif player1 == player2:
        print(player_1,":",player1)
        print(player_2,":",player2)
        print("Tie")
    print(player_1,"point",p1point)
    print(player_2,"point",p2point)
if p1point > p2point:
    print(player_1,"won the game")
elif p2point > p1point:
    print(player_2,"won the game")
else:
    print("The game is draw")
