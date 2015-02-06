from django.test import TestCase

from score.models import Game


class BowlingTest(TestCase):
    def setUp(self):
        self.game = Game()

    def roll_many(self, pins, count=20):
        [self.game.roll(pins) for i in range(count)]

    def test_gutter_game(self):
        self.roll_many(0)
        self.assertEqual(self.game.score(), 0)

    def test_simple_game(self):
        self.roll_many(1)
        self.assertEqual(self.game.score(), 20)
