## Chill or Unchill
# A game about keeping your cool
# Proudly presented by Nick Henegar
# Written for Python v 2.7.12

import madLists, random, textwrap
versionNumber = 1.02

def mainGame(player_name=''):
    wprint("Welcome to Chill or Unchill v." + str(versionNumber) + ", a text based adventure game where you make the important decisions.")
    if player_name == '':
        player_name = raw_input("\nFirst, what is your name, brave traveler? ").title()
    wprint("\nOk then, {}. You set out on your first adventure starting now. \nKeep your chill on lock.\n".format(player_name))
    # Begin game:
    # These are our victory/defeat condition values, as well as an optional secondary stat that
    # occassionally forces the player to do an action that will be detrimental to their unchill score (increasing it)
    chill = 0
    unchill = 0
    paranoia = 0
    dead = False
    # Loop for game
    # This keeps us going until a player either wins or dies trying.
    while not dead:
        q = procSit()
        chill, unchill, paranoia = answer(chill, unchill, paranoia, q)
        if unchill >= 10:
            dead = True
            wprint("You've reached a critical level of unchill. Karma kills you")
        if chill >= 420:
            dead = True
            wprint("Wow, you're quite a patient person, {}. You made it to the end of the game!".format(player_name))
    wprint("Final score: " + str(chill))
    # After the game is over, the player has the option to play it again, should they wish to do such a thing.
    playAgain(player_name)

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
    wprint(string)
    return q

    # Answer request and scoring
    # @params - requires 3 int variables to hold scores, as well as an int q-value to determine 'chillness' of a situation.
    # @returns - either normal() if below a certain paranoia threshold (5),
    #       or a chance to return paranoid() which increases as the paranoia increases 
def answer(chill, unchill, paranoia, q):
    response = raw_input("\nWhat do you do?").lower()
    if response == 'check stats':
        wprint("\nchill points: " + str(chill) + "\nunchill points: " + str(unchill) + "\nparanoia level: " + str(paranoia))
        return answer(chill, unchill, paranoia, q)
    elif (response != 'chill' and response != 'run' and response != 'smoke'):
        wprint("\nCurrently you can either chill, run, or smoke. You may also check your stats with 'check stats'")
        return answer(chill, unchill, paranoia, q)
    else:
        if (random.randint(0,paranoia) <= 5) :
            return normal(response, chill, unchill, paranoia, q)
        else:
            return paranoid(response, chill, unchill, paranoia, q)
    # Gives the normal scoring behaviors and textual feedback
    # @params - a string (response), which is collected from the user and validated before passing.
    # @params - our three scoring variables, as well as the q-value.
    # @returns - the scoring variables after modification
def normal(response, chill, unchill, paranoia, q):
    print ("\nYou " + response + '.')
    if (response == 'chill'):
        if (q < -3) :
            chill -= q
            unchill -= q
            wprint("\nThe situtation, however, is decidedly unchill. You have a bad time.")
        else :
            chill += q
            wprint("\nThings are relatively chill, you end up enjoying yourself.")
    elif (response == 'run'):
        if (q > 1) :
            unchill += q
            wprint("\nVery unchill, friend. That's how you hurt people's feelings.")
        else:
            chill += 2
            wprint("\nGood plan, that was spooky.")
    elif (response == 'smoke'):
        if (q < 0) :
            chill -= q
            paranoia -= q/2
            wprint("\nThe situation is unchill, but you get so high that you no longer care. Unfortunately, you're sketched out by the end of it.")
        else :
            chill += (q + 2)
            paranoia += q % 3
            wprint("\nYou end up having a great time and making a new friend, but your new friend keeps talking about " + madLists.para[random.randint(0,14)][0] +
                   ", which later give you some existential dread.")
    return chill, unchill, paranoia
    # This is randomly used if the player's paranoia level is too high from smoking too much.
    # @params - same as above.
    # @returns - same as above.
def paranoid(response, chill, unchill, paranoia, q):
    wprint("\nYou try to " + response + ", but you're feeling too paranoid.")
    wprint("\nYou accuse them of " + madLists.para[random.randint(0,14)][0])
    if (q < -5):
        unchill -= 5 * q
        wprint("\nYou're probably right, but now isn't a good time to say things like that. They react poorly.")
    elif (-5 < q < 0):
        unchill -= q
        wprint("\nThe truth hurts. Kind of mean, but you couldn't help yourself.")
    elif (0 <= q and q < 5):
        unchill += 2 * q
        wprint("\nThis earns you a nonplussed look as they leave you to your ravings.")
    else:
        chill += 3
        paranoia -= 5
        wprint("\nBut they laugh and think you are joking. Whew, that was close! You stop feeling as paranoid.")
          
    return chill, unchill, paranoia
    # Asks the player if they would like to play again.
    # if 'y' calls the main function again, otherwise it breaks.
def playAgain(player_name):
    choice = raw_input("\nWould you like to play again? (y/n) : ").lower()
    if choice == 'y':
        mainGame(player_name)
    else:
        wprint("I hope you enjoyed it!")
        print 'Goodbye!'
        exit()
    # This allows the text to be displayed in a pretty way
    # @depends - requires textwrap module to be loaded.
    # @params - any amount of text.
    # @returns - nicely formatted text.
def wprint(string):
    wrapped = textwrap.wrap(string)
    print ''
    for line in wrapped:
        print line

if __name__ == "__main__":
    mainGame()
