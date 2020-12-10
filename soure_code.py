import random 

move_list = ["rock", "paper", "scissor"]
computer = move_list[random.randint(0,2)]

def game1():
    print("Enter your move either R/P/S")
    player = False
    while player == False:
        player = input()
        player = player.lower()
       
        if player == "rock":
            if computer == "rock":
                print("Tie!")
            elif computer == "paper":
                print("You lose, computer use" + computer)
            elif computer == "scissor":
                print("You win computer used, " + computer)
        elif player == "paper":
            if computer == "rock":
                print("You win computer used, " + computer)
            elif computer == "paper":
                print("Tie")
            elif computer == "scissor":
                print("You lose computer used, " + computer)
        elif player == "scissor":
            if computer == "rock":
                print("You lose computer used, " + computer)
            elif computer == "paper":
                print("You win computer used, " + computer)
            elif computer == "scissor":
                print("Tie")
        else:
            print("invalid input, try again")
   
        
game = True
print("Let's play Rock, Paper, Scissors")
while game == True:
    game1()
    response = input("Do you want to play again y/n?")
    response = response.lower()
    if response == "y":
        game == True
        computer = move_list[random.randint(0,2)]
    elif response == "n":
        print("Thank you for playing")
        game == False
        break
    else:
        print("invalid response, try again")
        
        
    
            
    
