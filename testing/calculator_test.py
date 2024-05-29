from unittest import TestCase, main
from calculator import calculators

class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculators('2 + 2'), 4) # раскрывать подробный результат

    def test_minus(self):
        self.assertEqual(calculators('3 - 1'), 2)
    
    def test_multy(self):
        self.assertEqual(calculators('2 * 2'), 4)

    def test_divis(self):
        self.assertEqual(calculators('6 / 2'), 3)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculators('abracadabra')
        self.assertEqual('Выражение должно иметь хотя бы 1 знак (+-/*)', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculators('2 - 1 * 10')
        self.assertEqual('Выражение дожно иметь 2 числа и 1 знак', e.exception.args[0])
    
    def test_no_int(self):
        with self.assertRaises(ValueError) as e:
            calculators('NULL * 2')
        self.assertEqual('Выражение дожно иметь 2 числа и 1 знак', e.exception.args[0])
    
if __name__ == '__main__':
    main()