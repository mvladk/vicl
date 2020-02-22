from unittest import TestCase

from commands.SetTimer import SetTimer


class TestSetTimer(TestCase):
    def setUp(self):
        params = {"timer": 5}
        self.setTimer = SetTimer(params)

    def test_initial_seconds(self):
        self.assertEqual(self.setTimer.Timer.get_seconds(), 3)

    def test_run(self):
        self.setTimer.run()
        self.assertEqual(self.setTimer.Timer.get_seconds(), 5)

