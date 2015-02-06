from django.test import TestCase

from score.models import Game


class BowlingTest(TestCase):
    def setUp(self):
        self.game = Game()

    def roll_many(self, pins, count=20):
        for i in range(count):
            self.game.roll(pins)

    def assert_score(self, score):
        self.assertEqual(self.game.score(), score)

    def test_gutter_game(self):
        self.roll_many(0)
        self.assert_score(0)

    def test_all_ones(self):
        self.roll_many(1)
        self.assert_score(20)

    def test_single_spare(self):
        self.roll_many(5, count=3)
        self.roll_many(0, 17)
        self.assert_score(20)

    def test_single_strike(self):
        self.game.roll(10)
        self.roll_many(3, 2)
        self.roll_many(0, 16)
        self.assert_score(22)

    def test_perfect_game(self):
        self.roll_many(10, 12)
        self.assert_score(300)
