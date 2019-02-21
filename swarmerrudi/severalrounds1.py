import random

ownscore = 0
itsscore = 0
counter = 0
#input of your interaction
rounds = int(input("How many rounds would you like to play? "))
while counter <= (rounds+1):
    counter += 1
    answer = input("Answer Cooperate or Cheat: ")
#randomize opponent's cheating cooperation
    oanswer = random.choice(['Cooperate','Cheat'])
#scoreboard
    if answer == "Cooperate" and oanswer == "Cooperate":
        ownscore += 2
        itsscore += 2
    elif answer == "Cooperate" and oanswer == "Cheat":
        ownscore -= 1
        itsscore += 3
    elif answer == "Cheat" and oanswer == "Cooperate":
        ownscore += 3
        itsscore -= 1
    else:
        ownscore += 0
        itsscore += 0
    
    print('Your score is: \n %s \n whereas the opponent scored:  \n %s'%(ownscore, itsscore))

