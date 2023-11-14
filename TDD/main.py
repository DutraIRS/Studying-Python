import unittest
from module import feed_cat
from module import factorial

# Red -> Green -> Refactor
# Red: Write a test that fails
# Green: Write the simplest code to make the test pass
# Refactor: Clean up the code

class TestCatFunctions(unittest.TestCase):

    def test_feed_cat(self):
        self.assertEqual(feed_cat("Whiskers", "fish"), "Whiskers is happily eating fish")
        self.assertEqual(feed_cat("Garfield", "lasagna"), "Garfield is happily eating lasagna")
        self.assertEqual(feed_cat("Frajola", "Piu-piu"), "Frajola is happily eating Piu-piu")

class TestFactorial(unittest.TestCase):

    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_negative_number(self):
        self.assertRaises(ValueError, factorial, -13)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__":
    unittest.main()