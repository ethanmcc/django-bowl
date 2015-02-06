from django.test import TestCase

from score.models import Game


class BowlingTest(TestCase):
    def setUp(self):
        self.game = Game()

    def roll_many(self, pins, count=20):
        for roll in range(count):
            self.game.roll(pins)

    def assert_score(self, score):
        self.assertEqual(self.game.score(), score)

    def test_gutter_game(self):
        self.roll_many(0)
        self.assert_score(0)

    def test_all_ones(self):
        self.roll_many(1)
        self.assert_score(20)

    def test_sum_game(self):
        self.roll_many(3, 10)
        self.roll_many(4, 10)
        self.assert_score(70)

    def test_single_spare(self):
        self.roll_many(5, 3)
        self.roll_many(0, 17)
        self.assert_score(20)

    def test_single_strike(self):
        self.game.roll(10)
        self.roll_many(3, 2)
        self.roll_many(0, 17)
        self.assert_score(22)

    def test_perfect_game(self):
        self.roll_many(10, count=12)
        self.assert_score(300)

    def test_thirteen_strikes(self):
        self.roll_many(10, count=15)
        self.assert_score(300)
