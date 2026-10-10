import unittest
from calories import count_calories

class TestCountCalories(unittest.TestCase):

    def test_male_calories(self):
        result = count_calories(120, 80, 30, 60, "M")
        expected = (
            (-55.0969 + 0.6309 * 120 + 0.1988 * 80 + 0.2017 * 30)
            / 4.184
        ) * 60

        self.assertAlmostEqual(result, expected)