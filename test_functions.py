import unittest

from functions import MathFunctions, PersonFunctions
from person import Person


class TestMathFunctions(unittest.TestCase):

    def setUp(self):
        self.math = MathFunctions()

    def test_sum(self):
        my_sum = self.math.sum(43, 48)
        self.assertEqual(my_sum, 91)

    def test_difference(self):
        my_diff = self.math.difference(39, 2)
        self.assertEqual(my_diff, 37)

    def test_area(self):
        my_area = self.math.area(11, 7)
        self.assertEqual(my_area, 77)


class TestPersonFunctions(unittest.TestCase):

    def setUp(self):
        self.pf = PersonFunctions()

    def test_double_ages(self):
        pierre = Person("Pierre Landeau", 33)
        sarah = Person("Sarah Silverman", 38)
        people = [pierre, sarah]
        doubled_ages = self.pf.double_ages(people)

        self.assertEqual(doubled_ages[0].age, 66)
        self.assertEqual(doubled_ages[1].age, 76)

    def test_count_adults(self):
        adult = Person("Daniel Ne", 32)
        edge_case = Person("John Smith", 18)
        minor = Person("Jane Doe", 12)
        people = [adult, edge_case, minor]
        nb_adults = self.pf.count_adults(people)
        self.assertEqual(nb_adults, 2)

    def test_convert_to_dict(self):
        pierre = Person("Pierre Landeau", 33)
        sarah = Person("Sarah Silverman", 38)
        people = [pierre, sarah]
        dict_to_test = {"Pierre Landeau": 33,
                        "Sarah Silverman": 38}

        ppl_dict = self.pf.convert_to_dict(people)
        self.assertDictEqual(dict_to_test, ppl_dict)

    def test_remove_last_name(self):
        sandeep = Person("Sandeep Bandi", 25)
        self.pf.remove_last_name(sandeep)
        self.assertEqual("Sandeep", sandeep.name)

    def test_assign_grades_success(self):
        pierre = Person("Pierre Landeau", 33)
        sarah = Person("Sarah Silverman", 38)
        jane = Person("Jane Doe", 19)
        people = [pierre, sarah, jane]
        grades = [80, 77, 92]
        dict_to_test = {pierre: 80,
                        sarah: 77,
                        jane: 92}
        grades_dict = self.pf.assign_grades(people, grades)
        self.assertDictEqual(dict_to_test, grades_dict)

    def test_assign_grades_more_grades(self):
        pierre = Person("Pierre Landeau", 33)
        sarah = Person("Sarah Silverman", 38)
        people = [pierre, sarah]
        grades = [80, 77, 92]
        self.assertRaises(IndexError, self.pf.assign_grades, people, grades)

    def test_assign_grades_more_people(self):
        pierre = Person("Pierre Landeau", 33)
        sarah = Person("Sarah Silverman", 38)
        jane = Person("Jane Doe", 19)
        people = [pierre, sarah, jane]
        grades = [80, 77]
        self.assertRaises(IndexError, self.pf.assign_grades, people, grades)




