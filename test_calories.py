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

    def test_female_calories(self):
        result = count_calories(120, 60, 25, 45, "F")
        expected = (
                           (-20.4022 + 0.4472 * 120 - 0.1263 * 60 + 0.0740 * 25)
                           / 4.184
                   ) * 45

        self.assertAlmostEqual(result, expected)

    def test_negative_duration(self):
        with self.assertRaises(ValueError):
            count_calories(120, 70, 30, -10, "M")


    def test_zero_duration(self):
        result = count_calories(120, 70, 30, 0, "M")
        self.assertEqual(result, 0)

if __name == "__main__":
    unittest.main()