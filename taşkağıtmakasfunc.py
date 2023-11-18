import random
import time
raund = int(input("How many raunds do you want to play: "))
options =("rock","paper","scissors")
raund2 = 0
player_1, player_2= "Ahmet", "None"
p1point, p2point = 0, 0 
def function(a, b):
    global p1point,p2point
    if (a == "rock" and b == "paper")or (a == "scissors" and b == "rock") or (a == "paper" and b == "scissors"):
        print(player_1,":",a)
        print(player_2,":",b)
        p2point += 1
        print(f"{raund2}.raund winner is {player_2}")
        print(player_2,"win")
        print(p1point,"-",p2point)     
    elif (b == "rock" and a == "paper")or (b == "scissors" and a == "rock") or (b == "paper" and a == "scissors"):
        print(player_1,":",a)
        print(player_2,":",b)
        p1point += 1
        print(raund2,".raund winner is"," ",player_1,sep="")
        print(player_1,"win")
        print(p1point,"-",p2point)
    else:
        print(player_1,":",a)
        print(player_2,":",b)
        print(raund2,".raund is Tie",sep="")
        print(p1point,"-",p2point)
while raund2 < raund:
    time.sleep(1)
    print(f"{raund2+1}.raund")
    raund2 += 1
    player1, player2 = options[random.randint(0,2)], options[random.randint(0,2)]
    function(player1, player2)
print(f"General score = {player_1}={p1point}\n                {player_2}={p2point}")