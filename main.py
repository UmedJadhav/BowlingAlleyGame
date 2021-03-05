from constants import STRIKE_SYMBOL, SPARE_SYMBOL , MISS_SYMBOL

def declare_winner(winner):
    print()

def display_scorecard(players):
    print()
    print('-- ScoreCard ---')
    print()
    for idx, player in enumerate(players):
        print()

if __name__ == '__main__':
    score_calc = Score_Calculator()
    bowling_game = Bowling_Game(score_calc)
    
    print(f"Welcome to the Bowling Alley !!")

    no_of_players = int(input('Enter the number of Players: '))
    players = []

    for idx in range(no_of_players):
        player_name = input('Enter player name: ')
        players.append(Player(player_name))
    
    print()
    print(f"** Use {STRIKE_SYMBOL} for STRIKE, {SPARE_SYMBOL} for SPARE , {MISS_SYMBOL} for a MISS **")
    print()


