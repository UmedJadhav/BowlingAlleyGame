from Roll.roll_parser import Roll_Parser


class Bowling_Game:
    def __init__(self, score_calc):
        self._roll_parser = Roll_Parser()

    
    def score_of_game(self, input):
        parsed_roll = self._roll_parser.parse(input)


