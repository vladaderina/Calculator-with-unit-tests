from unittest import TestCase, main
from calc import calc

class calcTest(TestCase):
    def test_plus(self):
        self.assertEqual(calc('4+4'), 8)
    def test_multy(self):
        self.assertEqual(calc('4*8'), 32)
    def test_minus(self):
        self.assertEqual(calc('8-7'), 1)
    def test_dev(self):
        self.assertEqual(calc('4/4'), 1)
    def test_no_sign(self):
        with self.assertRaises(ValueError) as e:
            calc('434')
        self.assertEqual("Выражение должно содержать оператор", e.exception.args[0])
    def test_mixed_symb(self):
        with self.assertRaises(ValueError) as e:
            calc('44+')
        self.assertEqual("Выражение должно содержать только 2 целых числа и 1 знак", e.exception.args[0])
    def test_many_sign(self):
        with self.assertRaises(ValueError) as e:
            calc('15/4+')
        self.assertEqual("Выражение должно содержать только 2 целых числа и 1 знак", e.exception.args[0])
    def test_str(self):
        with self.assertRaises(ValueError) as e:
            calc('a+b')
        self.assertEqual("Выражение должно содержать только 2 целых числа и 1 знак", e.exception.args[0])
    def test_float(self):
        with self.assertRaises(ValueError) as e:
            calc('a+b')
        self.assertEqual("Выражение должно содержать только 2 целых числа и 1 знак", e.exception.args[0])
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError) as e:
            calc('3/0')
        self.assertEqual("Выражение не должно делиться на 0", e.exception.args[0])
if __name__ == '__main__':
    main()