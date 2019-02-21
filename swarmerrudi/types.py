import random

ownscore = 0
itsscore = 0
counter = 0

#types
def random():
    oanswer = random.choice(['Cooperate','Cheat'])

def always_cheat():
    oanswer = "Cheat"

def always_cooperate():
    oanswer = "Cooperate"

def copycat():

def grudger():

def detective():


def main():
#scoreboard
    rounds = int(input("How many rounds would you like to play? "))
    type = int(input("Who do you want to fight? n\ (1) random n\ (2) copycat n\ (3) cheater n\ (4) cooperater n\ (5) grudger n\ (6) detective"))
    while counter <= (rounds+1):
        counter += 1
        answer = input("Answer Cooperate or Cheat: ") #change to match other types against each other
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

main()
