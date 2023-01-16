#!/usr/bin/python3
import unittest
import io
import sys
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
            Rectangle({"a": 1, "b": 5}, 5)

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
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 5)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
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
            Rectangle(2, {"a": 1, "b": 5})

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
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -5)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)


class TestRectangleClass_x(unittest.TestCase):

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, "haile")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 5, 32.67)

    def test_dist_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {"a": 1, "b": 5})

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, [2, 4])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 2, (1, 4))

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {1, 3})

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 5, range(5))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 1, -5)


class TestRectangleClass_y(unittest.TestCase):

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 5, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 3, "haile")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 5, 3, 32.67)

    def test_dist_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 2, {"a": 1, "b": 5})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 3, 1, [2, 4])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 2, 1, (1, 4))

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 1, {1, 3})

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 5, 1, range(5))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 1, 2, -6)


class TestRectangleClass_area(unittest.TestCase):

    def test_area(self):
        self.assertEqual(10, Rectangle(2, 5).area())

    def test_area_rectangle(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_change(self):
        r = Rectangle(10, 2, 0, 0, 0)
        r.width = 7
        r.height = 10
        self.assertEqual(70, r.area())

    def test_area_value_input(self):
        with self.assertRaises(TypeError):
            print(Rectangle(1, 4).area(10))


class TestRectangleClass_str(unittest.TestCase):

    def test_str(self):
        rs1 = Rectangle(4, 1, 3, 6, 9)
        s = '[Rectangle] ({}) 3/6 - 4/1'.format(rs1.id)
        self.assertEqual(s, str(rs1))

    def test__str__(self):
        rs2 = Rectangle(1, 2, 3, 4, 5)
        s = '[Rectangle] ({}) 3/4 - 1/2'.format(rs2.id)
        self.assertEqual(s, rs2.__str__())

    def test__str__input(self):
        rs3 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            print(rs3.__str__(1))

    def test_str_default(self):
        rs4 = Rectangle(1, 2)
        s = '[Rectangle] ({}) 0/0 - 1/2'.format(rs4.id)
        self.assertEqual(s, str(rs4))


class TestRectangleClass_display(unittest.TestCase):

    def test_display(self):
        rd1 = Rectangle(3, 2)
        capture = io.StringIO()
        sys.stdout = capture
        rd1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("###\n###\n", capture.getvalue())

    def test_display_error(self):
        rd2 = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            print(rd2.display(2))

    def test_display_all_param(self):
        rd3 = Rectangle(3, 5)
        capture = io.StringIO()
        sys.stdout = capture
        rd3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("###\n###\n###\n###\n###\n", capture.getvalue())

    def test_display_x(self):
        rd4 = Rectangle(3, 3, 1)
        c = io.StringIO()
        sys.stdout = c
        rd4.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(" ###\n ###\n ###\n", c.getvalue())

    def test_display_y(self):
        rd5 = Rectangle(3, 2, 1, 2)
        c = io.StringIO()
        sys.stdout = c
        rd5.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("\n\n ###\n ###\n", c.getvalue())


class TestRectangleClass_update_args(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 10, 10, 10)

    def tearDown(self):
        pass

    def test_update_arg_1_param(self):
        self.r1.update(8)
        self.assertEqual('[Rectangle] (8) 10/10 - 10/10', str(self.r1))

    def test_update_arg_2_param(self):
        self.r1.update(8, 4)
        self.assertEqual('[Rectangle] (8) 10/10 - 4/10', str(self.r1))

    def test_update_arg_3_param(self):
        self.r1.update(8, 4, 5)
        self.assertEqual('[Rectangle] (8) 10/10 - 4/5', str(self.r1))

    def test_update_arg_4_param(self):
        self.r1.update(8, 4, 5, 9)
        self.assertEqual('[Rectangle] (8) 9/10 - 4/5', str(self.r1))

    def test_update_arg_5_param(self):
        self.r1.update(8, 4, 5, 9, 12)
        self.assertEqual('[Rectangle] (8) 9/12 - 4/5', str(self.r1))

    def test_update_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r1.update(1, "hi")

    def test_update_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r1.update(1, range(5))

    def test_update_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r1.update(1, -1)

    def test_update_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r1.update(1, 0)

    def test_udpate_zero_x(self):
        self.r1.update(1, 2, 3, 0)
        self.assertEqual('[Rectangle] (1) 0/10 - 2/3', str(self.r1))


class TestRectangleClass_update_args(unittest.TestCase):

    def setUp(self):
        self.r2 = Rectangle(10, 10, 10, 10)

    def tearDown(self):
        pass

    def test_update_kwarg_1_param(self):
        self.r2.update(id=7)
        self.assertEqual('[Rectangle] (7) 10/10 - 10/10', str(self.r2))

    def test_update_kwarg_2_param(self):
        self.r2.update(id=7, width=7)
        self.assertEqual('[Rectangle] (7) 10/10 - 7/10', str(self.r2))

    def test_update_kwarg_3_param(self):
        self.r2.update(id=7, width=7, height=20)
        self.assertEqual('[Rectangle] (7) 10/10 - 7/20', str(self.r2))

    def test_update_kwarg_4_param(self):
        self.r2.update(id=7, width=7, height=20, x=6)
        self.assertEqual('[Rectangle] (7) 6/10 - 7/20', str(self.r2))

    def test_update_kwarg_5_param(self):
        self.r2.update(id=7, width=7, height=20, x=6, y=23)
        self.assertEqual('[Rectangle] (7) 6/23 - 7/20', str(self.r2))

    def test_update_kwarg_change_order(self):
        self.r2.update(x=6, y=23, width=7, height=20, id=7)
        self.assertEqual('[Rectangle] (7) 6/23 - 7/20', str(self.r2))

    def test_update_kwarg_empty(self):
        self.r2.update()
        x = self.r2.id
        s = '[Rectangle] ({}) 10/10 - 10/10'.format(x)
        self.assertEqual(s, str(self.r2))

    def test_update_kwarg_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r2.update(width="haile")

    def test_update_kwarg_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r2.update(height=range(5))

    def test_udpate_kwarg_neative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r2.update(width=-2)

    def test_update_kwarg_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r2.update(height=0)


if __name__ == '__main__':
    unittest.main()
