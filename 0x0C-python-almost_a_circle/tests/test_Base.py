import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_constructor(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_constructor_input(self):
        b3 = Base(-4)
        self.assertEqual(b3.id, -4)
        b4 = Base(13)
        self.assertEqual(b4.id, 13)

if __name__ == '__main__':
    unittest.main()
