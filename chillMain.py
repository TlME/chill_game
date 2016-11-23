## Chill or Unchill
# A game about keeping your cool
# Proudly presented by Nick Henegar
# Written for Python v 2.7.12

def mainGame(player_name=''):
    print("Welcome to Chill or Unchill, a text based adventure game where you make the important decisions.")
    if player_name == '':
        player_name = raw_input("\nFirst, what is your name, brave traveler? ").title()
        if player_name == 'Snoop Dogg':
            win(player_name)
    print("\nOk then, {}. You set out on your first adventure starting now. Keep your chill on lock.".format(player_name))
    
