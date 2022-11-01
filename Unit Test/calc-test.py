import calc
import unittest


# Parte que o Professor mandou a gente só decorar por enquanto
def setUpModule():
    print('\nExecuting SetUpModule')

def tearDownModule():
    print('\nExecuting TearDownModule')

class TestModuleQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\nExecuting SetUpClass')

    @classmethod
    def tearDownClass(cls):
        print('\nExecuting TearDownClass')

    def setUp(self):
        print('\nExecuting SetUpMethod')

    def tearDown(self):
        print('\nExecuting TearDownMethod')
      
    # Testes da função add  
    def test_case_add_ints_positive_positive(self):
        print('\nExecuting Case Test: Integers - Positive - Positive')
        self.assertEqual(calc.add(1, 1), 2)

    def test_case_add_ints_negative_negative(self):
        print('\nExecuting Case Test: Integers - Negative - Negative')
        self.assertEqual(calc.add(-1, -1), -2)

    def test_case_add_floats_positive_positive(self):
        print('\nExecuting Case Test: Floats - Positive - Positive')
        self.assertAlmostEqual(calc.add(1.0, 1.5), 2.5, 5)
        print('\n', ':) '*42, '\n', sep='')

    # Testes da função subtract
    def test_case_subtract_ints_positive_positive(self):
        print('\nExecuting Case Test: Integers - Positive - Positive')
        self.assertEqual(calc.subtract(1, 1), 0)

    def test_case_subtract_ints_negative_negative(self):
        print('\nExecuting Case Test: Integers - Negative - Negative')
        self.assertEqual(calc.subtract(-1, -2), 1)

    def test_case_subtract_floats_positive_positive(self):
        print('\nExecuting Case Test: Floats - Positive - Positive')
        self.assertAlmostEqual(calc.subtract(1.0, 1.5), -0.5, 5)
        print('\n', ':) '*42, '\n', sep='')

    # Testes da função multiply
    def test_case_multiply_ints_positive_positive(self):
        print('\nExecuting Case Test: Integers - Positive - Positive')
        self.assertEqual(calc.multiply(1, 1), 1)

    def test_case_multiply_ints_negative_negative(self):
        print('\nExecuting Case Test: Integers - Negative - Negative')
        self.assertEqual(calc.multiply(-1, -2), 2)

    def test_case_multiply_floats_positive_positive(self):
        print('\nExecuting Case Test: Floats - Positive - Positive')
        self.assertAlmostEqual(calc.multiply(1.0, 1.5), 1.5, 5)
        print('\n', ':) '*42, '\n', sep='')

    # Testes da função divide
    def test_case_divide_ints_positive_positive(self):
        print('\nExecuting Case Test: Integers - Positive - Positive')
        self.assertEqual(calc.divide(1, 1), 1)

    def test_case_divide_ints_negative_negative(self):
        print('\nExecuting Case Test: Integers - Negative - Negative')
        self.assertEqual(calc.divide(-1, -2), 0.5)

        # Teste divisão por 0
    def test_case_divide_divide_by_zero(self):
        print('\nExecuting Case Test: Division by zero')
        self.assertRaises(ValueError, calc.divide, 1, 0)
        print('\n', ':) '*42, '\n', sep='')

    # Testes da função exp
    def test_case_exp_ints_positive_positive(self):
        print('\nExecuting Case Test: Integers - Positive - Positive')
        self.assertEqual(calc.exp(10, 1), 1)

    def test_case_exp_ints_negative_negative(self):
        print('\nExecuting Case Test: Integers - Negative - Negative')
        self.assertEqual(calc.exp(-2, -10), 0.01)

    def test_case_exp_floats_positive_positive(self):
        print('\nExecuting Case Test: Floats - Positive - Positive')
        self.assertAlmostEqual(calc.exp(1.5, 1.0), 1.0, 5)
        print('\n', ':) '*42, '\n', sep='')

if __name__ == '__main__':
    unittest.main(verbosity=3)