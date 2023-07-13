import unittest
import calculator

class Test_calculator(unittest.TestCase):

    def test_add(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.add(1, 5), 6, "Sum is not adding to what it should")
        self.assertEqual(calc.add(1), 1, "Sum is not adding to what it should")
        self.assertEqual(calc.add(99, 200, 1, 1, 1), 302, "Sum is not adding to what it should")
        self.assertEqual(calc.add(8, 1000), 1008, "Sum is not adding to what it should")
        self.assertNotEqual(calc.add(1, 3), 6, "Sum is equal where it should not")
        with self.assertRaises(Exception):
            calc.add("1", "3")
# run the test
unittest.main()
