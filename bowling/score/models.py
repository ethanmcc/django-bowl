# from django.db import models


class Game():
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def get_next_head(self):
        for index in range(len(self.rolls)):
            yield self.rolls[index:]

    @staticmethod
    def is_strike(roll):
        return roll[0] == 10

    @staticmethod
    def is_spare(roll):
        return sum(roll[:2]) == 10

    def score(self):
        total = 0
        frame = 0
        rolls = self.get_next_head()
        for roll in rolls:
            frame += 1
            if frame > 10:
                break
            if self.is_strike(roll):
                total += sum(roll[:3])
            elif self.is_spare(roll):
                total += sum(roll[:3])
                next(rolls)
            else:
                total += sum(roll[:2])
                next(rolls)
        return total
