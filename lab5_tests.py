import data
import lab5
import unittest
from data import Time


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        time1 = data.Time(5, 23, 21)
        time2 = data.Time(1, 32, 49)
        expected=Time(6,56,10)
        input = lab5.time_add(time1, time2)
        self.assertEqual(expected, input)

    def test_time_add_2(self):
        time1 = data.Time(21, 00, 60)
        time2 = data.Time(1, 59, 180)
        expected=Time(23,3,0)
        input = lab5.time_add(time1, time2)
        self.assertEqual(expected, input)

    # Part 4
    def test_is_descending(self):
        list1 = [52,23,43,32]
        expected = False
        input = lab5.is_descending(list1)
        self.assertEqual(expected, input)

    def test_is_descending_2(self):
        list1 = [54,43,32,21]
        expected = True
        input = lab5.is_descending(list1)
        self.assertEqual(expected, input)

    # Part 5
    def test_largest_between(self):
        list1 = [54,43,32,21,123,51,3,6,12,6,2]
        expected = 4
        input = lab5.largest_between(list1,2,7)
        self.assertEqual(expected, input)

    def test_largest_between_2(self):
        list1 = [54,43,32,21,2,51,3,6,12,6,2]
        expected = 5
        input = lab5.largest_between(list1,1,10)
        self.assertEqual(expected, input)

    # Part 6
    def test_furthest_from_origin(self):
        point1= data.Point(5, 5)
        point2= data.Point(1, 6)
        point3= data.Point(7, 2)
        point4= data.Point(3, 5)
        points_list=[point1,point2,point3,point4]
        expected=point3
        self.assertEqual(expected, lab5.furthest_from_origin(points_list))

    def test_furthest_from_origin_2(self):
        point1= data.Point(241, 421)
        point2= data.Point(262, 342)
        point3= data.Point(234, 346)
        point4= data.Point(521, 5)
        points_list=[point1,point2,point3,point4]
        expected=point4
        self.assertEqual(expected, lab5.furthest_from_origin(points_list))


if __name__ == '__main__':
    unittest.main()
