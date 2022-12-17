import unittest
from employee11_3 import Employee


class TestEmployee(unittest.TestCase):
    """Test for the class employee"""
    def setUp(self):
        """Creates test methods for a default and custom raise"""
        self.employee = Employee('Dave', 'McIntosh', 60000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(65000, self.employee.annual_salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(2500)
        self.assertEqual(62500, self.employee.annual_salary)
