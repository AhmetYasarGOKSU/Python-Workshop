import random 
import time
raund = int(input("How many raunds do you want to play: "))
raund2 = 0
options =("rock","paper","scissors")
player_1 = "Ahmet"
player_2 = "None"
p1point = 0 
p2point = 0
while raund2 < raund:
    time.sleep(1)
    raund2 += 1
    player1 = options[random.randint(0,2)]
    player2 = options[random.randint(0,2)]
    if player1 == "rock" and player2 == "scissors":
        print(player_1,":",player1)
        print(player_2,":",player2)
        p1point += 1
        print(raund2,".raund winner is"," ",player_1,sep="")
    elif player1 == "rock" and player2 == "paper":
        print(player_1,":",player1)
        print(player_2,":",player2)
        p2point += 1
        print(raund2,".raund winner is"," ",player_2,sep="")
    elif player1 == "paper" and player2 == "rock":
        print(player_1,":",player1)
        print(player_2,":",player2)
        p1point += 1
        print(raund2,".raund winner is"," ",player_1,sep="")
    elif player1 == "paper" and player2 == "scissors":
        print(player_1,":",player1)
        print(player_2,":",player2) 
        p2point += 1
        print(raund2,".raund winner is"," ",player_2,sep="")
    elif player1 == "scassers" and player2 == "rock":
        print(player_1,":",player1)
        print(player_2,":",player2)
        p2point += 1
        print(raund2,".raund winner is"," ",player_2,sep="")
    elif player1 == player2:
        print(player_1,":",player1)
        print(player_2,":",player2)
        print(raund2,".raund is Tie",sep="")
    print(player_1,"point",p1point)
    print(player_2,"point",p2point)
if p1point > p2point:
    print(player_1,"won the game")
elif p2point > p1point:
    print(player_2,"won the game")
else:
    print("The game is draw")
