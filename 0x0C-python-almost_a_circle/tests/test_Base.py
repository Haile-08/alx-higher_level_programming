import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):

    def test_class_instance(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_class_instance_with_none(self):
        b3 = Base(None)
        b4 = Base()
        self.assertEqual(b3.id, b4.id - 1)

    def test_class_attribute(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)

    def test_Class_attribute_input(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_objects)

    def test_class_attr(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_with_string_input(self):
        b5 = Base("haile")
        self.assertEqual(b5.id, "haile")

    def test_with_float_input(self):
        b6 = Base(2.9)
        self.assertEqual(b6.id, 2.9)

    def test_for_class(self):
        b7 = Base()
        self.assertIsInstance(b7, Base)

    def test_for_more_than_1_arg(self):
        with self.assertRaises(TypeError):
            print(Base(1, 3))


if __name__ == '__main__':
    unittest.main()
