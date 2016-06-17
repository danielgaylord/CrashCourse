import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.test_emp = Employee("Dan", "Gaylord", 60000)
        self.amount = 10000

    def test_give_default_raise(self):
        self.test_emp.give_raise()
        self.assertEqual(self.test_emp.salary, 65000)

    def test_give_custom_raise(self):
        self.test_emp.give_raise(self.amount)
        self.assertEqual(self.test_emp.salary, 70000)

if __name__ == "__main__":
    unittest.main()
