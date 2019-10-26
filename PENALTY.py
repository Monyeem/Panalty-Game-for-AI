import random
direction=["left","middle","right"]
totalPenalties=0
userTeamScore=0
computerTeamScore=0
print("      -------------------------------")
print("      |                              |")
print("      |              0               |")
print("      |             /|\              |")
print("      |              |               |")
print("      |             / \              |")
print("-----------------------------------------------")
print("****WELCOME TO THE PYTHON PENALTY SHOOTOUT****")
print("Choose left,right or middle to score or make save")

def penaltyFor():
    global totalPenalties
    global userTeamScore
    totalPenalties+=1
    playerShotDirection=input("Pick your Spot:").lower()
    keeperDive=random.choice(direction)
    print("Goal-keeper dives to the "+ keeperDive.upper())
    if playerShotDirection=="left" and keeperDive=="right":
        print ("Trying to be smart and clever. It's a Save!!!")
    elif playerShotDirection=="right" and keeperDive=="left":
        print ("That is ridiculous. It's a Save!!!")
    elif playerShotDirection=="middle" and keeperDive=="middle":
        print ("Ohhhh, brillant.It's a Save!!!")
    else:
        print("Toppp Corner. GOOOAAALLLLL!!!!!!!")
        userTeamScore+=1

def penaltyAgainst():
    global totalPenalties
    global computerTeamScore
    totalPenalties+=1
    playerKeeperDive=input("Choose dive direction:").lower()
    computerShotDirection=random.choice(direction)
    print ("Computer hits the ball to the "+computerShotDirection)
    if computerShotDirection=="left" and playerKeeperDive=="right":
        print ( "That is ridiculous. It's a SAVE!!!")
    elif computerShotDirection=="right" and playerKeeperDive=="left":
        print ("Ohhhh, brillant.It's a Save!")
    elif computerShotDirection=="middle" and playerKeeperDive=="middle":
        print ("Trying to be smart and clever. It's a Save!!!")
    else:
        print("What a Goalll!!!!")
        computerTeamScore+=1

def printScores():
    print("The score is now USER:"+str(userTeamScore)+" "+"COMPUTERr:"+str(computerTeamScore))

def finalScore():
    print("FINAL SCORE "+str(userTeamScore) +"-" +str(computerTeamScore)) 
    if userTeamScore>computerTeamScore:
        print ("Well done, you are the winner")
    elif userTeamScore==computerTeamScore:
        print("A draw")
    else:
        print("You Lost the Penalty Shoot-Out") 
    
while totalPenalties<4:
    penaltyFor()
    penaltyAgainst()
    printScores()
    
finalScore()
    