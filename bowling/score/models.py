class Game(object):
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def is_strike(self, rolls):
        return rolls[0] == 10

    def is_spare(self, rolls):
        return sum(rolls[:2]) == 10

    def score(self, rolls=None, frame=1):
        if rolls is None:
            rolls = self.rolls

        if frame > 10:
            return 0
        frame += 1

        if self.is_strike(rolls):
            return sum(rolls[:3]) + self.score(rolls[1:], frame)
        elif self.is_spare(rolls):
            return sum(rolls[:3]) + self.score(rolls[2:], frame)
        else:
            return sum(rolls[:2]) + self.score(rolls[2:], frame)
