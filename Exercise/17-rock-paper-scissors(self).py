import random

class Janken:
    def Shuffle(self):
        random.shuffle(options)
    
    
game = True
options = ["rock", "paper", "scissor"]
janken = Janken()
score = 0
pc_score = 0
janken.Shuffle()

while game:
    move = input("Rock, Paper or Scissor?: (q to quit)").lower()
    if move == "q":
        break
    elif move not in options:
        print("Invalid option")
    elif move == options[0]:
        print("Tie!")
        janken.Shuffle()
    elif move == "rock" and options[0] == "scissor" or move == "paper" and options[0] == "rock" or move == "scissor" and options[0] == "paper":
        print(f"You: {move}")
        print()
        print(f"PC: {options[0]}")
        print("You win!")
        score +=1
        janken.Shuffle()
        print(f"The score is {score}:{pc_score}")
        if score >= 3 or pc_score >= 3:
            print("GAME OVER")
            break
        else:
            continue
    # elif move == "rock" and options == "paper" or move == "paper" and options == "scissor" or move == "scissor" and options == "rock": 
    #     print("You lost!")
    #     pc_score +=1
    #     janken.Shuffle()
    #     print(f"The score is {score}:{pc_score}")
    else:
        print(f"You: {move}")
        print()
        print(f"PC: {options[0]}")
        print("You lost!")
        pc_score +=1
        janken.Shuffle()
        print(f"The score is {score}:{pc_score}")
        if score >= 3 or pc_score >= 3:
            print("GAME OVER")
            break
        else:
            continue




