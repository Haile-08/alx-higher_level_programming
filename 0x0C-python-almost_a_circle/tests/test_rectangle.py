import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass_init(unittest.TestCase):

    def test_class_id(self):
        r1 = Rectangle(1, 3)
        r2 = Rectangle(3, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_class_param_no_input(self):
        with self.assertRaises(TypeError):
            print(Rectangle().id)

    def test_class_param_input_over(self):
        with self.assertRaises(TypeError):
            print(Rectangle(1, 2, 4, 5, 5, 6).id)

    def test_class_input_id(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_class_string_input(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, "haile").id, "haile")

    def test_class_float_input(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 6.7).id, 6.7)

    def test_class_list_input(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, [1, 2]).id, [1, 2])

    def test_class_attribut(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__nb_objects)

    def test_class_instance(self):
        self.assertNotIsInstance(Rectangle, Base)

    def test_class_isinstance(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_class_private_att_w(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__width)

    def test_class_private_att_h(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__height)

    def test_class_private_att_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 5, 6).__x)

    def test_class_private_att_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 5, 6).__y)


class TestRectangleClass_width(unittest.TestCase):

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 3)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("haile", 4)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(32.67, 5)

    def test_dist_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a":1, "b":5}, 5)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 4], 6)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 4), 5)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 3}, 5)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 5)

    def test_negative_width(self):
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            Rectangle(-3, 5)

    def test_zero_width(self):
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            Rectangle(0, 5)


class TestRectangleClass_height(unittest.TestCase):

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "haile")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, 32.67)

    def test_dist_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a":1, "b":5})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [2, 4])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, (1, 4))

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 3})

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, range(5))

    def test_negative_height(self):
        with self.assertRaisesRegex(TypeError, "height must be > 0"):
            Rectangle(3, -5)

    def test_zero_height(self):
        with self.assertRaisesRegex(TypeError, "height must be > 0"):
            Rectangle(3, 0)


class TestRectangleClass_x(unittest.TestCase):

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)
