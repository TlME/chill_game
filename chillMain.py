## Chill or Unchill
# A game about keeping your cool
# Proudly presented by Nick Henegar
# Written for Python v 2.7.12

import madLists, random
versionNumber = 1.02

def mainGame(player_name=''):
    print("Welcome to Chill or Unchill v." + str(versionNumber) + ", a text based adventure game where you make the important decisions.")
    if player_name == '':
        player_name = raw_input("\nFirst, what is your name, brave traveler? ").title()
    print("\nOk then, {}. You set out on your first adventure starting now. Keep your chill on lock.".format(player_name))
    #Begin game:
    chill = 0
    unchill = 0
    paranoia = 0
    dead = False
    #Loop for game
    while not dead:
        q = procSit()
        chill, unchill, paranoia = answer(chill, unchill, paranoia, q)
        if unchill >= 10:
            dead = True
            print("You've reached a critical level of unchill. Karma kills you")
        if chill >= 420:
            dead = True
            print("Wow, you're quite a patient person, {}. You made it to the end of the game!".format(player_name))
    print("Final score: " + str(chill))
    playAgain(player_name)
    #end game

    # Procedural Situation Gen
    # @params - requires madLists to be loaded
    # @returns - q, the sum of weighted chillness values
def procSit():
    #to-do: create list for encounter intro
    string = ''
    q = 0
    for i in range(0,5):
        j = random.randint(0,19)
        string += madLists.procList[i][j][0]
        q += madLists.procList[i][j][1]
    print "\n" + string
    return q

    # Answer request and scoring
def answer(chill, unchill, paranoia, q):
    response = raw_input("\nWhat do you do?").lower()
    if response == 'check stats':
        print("\nchill points: " + str(chill) + "\nunchill points: " + str(unchill) + "\nparanoia level: " + str(paranoia))
        return answer(chill, unchill, paranoia, q)
    elif (response != 'chill' and response != 'run' and response != 'smoke'):
        print("\nCurrently you can either chill, run, or smoke.")
        return answer(chill, unchill, paranoia, q)
    else:
        if (random.randint(0,paranoia) <= 5) :
            return normal(response, chill, unchill, paranoia, q)
        else:
            return paranoid(response, chill, unchill, paranoia, q)
def normal(response, chill, unchill, paranoia, q):
    print ("\nYou " + response + '.')
    if (response == 'chill'):
        if (q < -3) :
            chill -= q
            unchill -= q
            print("\nThe situtation, however, is decidedly unchill. You have a bad time.")
        else :
            chill += q
            print("\nThings are relatively chill, you end up enjoying yourself.")
    elif (response == 'run'):
        if (q > 1) :
            unchill += q
            print("\nVery unchill, friend. That's how you hurt people's feelings.")
        else:
            chill += 2
            print("\nGood plan, that was spooky.")
    elif (response == 'smoke'):
        if (q < 0) :
            chill -= q
            paranoia -= q/2
            print("\nThe situation is unchill, but you get so high that you no longer care. Unfortunately, you're sketched out by the end of it.")
        else :
            chill += (q + 2)
            paranoia += q % 3
            print("\nYou end up having a great time and making a new friend,\n but your new friend keeps talking about " + madLists.para[random.randint(0,14)][0] +
                   ",\n which later give you some existential dread.")
    return chill, unchill, paranoia
# This is randomly used if the player's paranoia level is too high from smoking too much.
def paranoid(response, chill, unchill, paranoia, q):
    print("\nYou try to " + response + ", but you're feeling too paranoid.")
    print("\nYou accuse them of " + madLists.para[random.randint(0,14)][0])
    if (q < -5):
        unchill -= 5 * q
        print("\nYou're probably right, but now isn't a good time to say things like that. They react poorly.")
    elif (-5 < q < 0):
        unchill -= q
        print("\nThe truth hurts. Kind of mean, but you couldn't help yourself.")
    elif (0 <= q and q < 5):
        unchill += 2 * q
        print("\nThis earns you a nonplussed look as they leave you to your ravings.")
    else:
        chill += 3
        paranoia -= 5
        print("\nBut they laugh and think you are joking. Whew, that was close! You stop feeling as paranoid.")
          
    return chill, unchill, paranoia

def playAgain(player_name):
    choice = raw_input("\nWould you like to play again? (y/n) : ").lower()
    if choice == 'y':
        mainGame(player_name)
    else:
        print("I hope you enjoyed it!")
        print 'Goodbye!'
if __name__ == "__main__":
    mainGame()
