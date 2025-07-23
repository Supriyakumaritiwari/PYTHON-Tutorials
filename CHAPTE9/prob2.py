#the game() function in program lets a user play a game and returns a sore of an integer . you need to read a file 'hi-score.txt' which is either blank or contains the previous Hi-score . you need to wap to updatethe Hi-score hwnever the game ()breake the high score
# 
import random


def game():
    print("You are playing the game.....")
    score = random.randint(1,62)
    #fetch the Hi-score file
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your Score: {score}")
    if(score>hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score

game()