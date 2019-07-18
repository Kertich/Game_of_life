class Game_of_Life:
    def __init__(self, start, rules, high_score):
        self.start = start
        self.rules = rules
        self.high_score = high_score
    def run_game_of_life(self, it):
        current = self.start
        previous_score = None
        score = []
        i = 0
        while (not current.equals(previous_score) and i < it):
            i += 1
            previous_score = current.copy()
            score.append(previous_score.grid)
            current = current.apply_rules(self.rules,self.high_score)
        score.append(current.grid)
        return score