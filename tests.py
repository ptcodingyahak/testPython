# tests.py
import unittest
import calculator


class MycalculatorTest (unittest.TestCase):

    def testAdd(self):  #test fucntion
        result = calculator.add(10, 20)
        self.assertEqual(result, 30)

    def testSubstract(slef):
        result = calculator.substract(20, 10)
        self.assertEqual(result, 10)

# unittest start
if __name__=='__main__':
    unittest.main()
