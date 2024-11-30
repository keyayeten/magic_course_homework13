# Помимо методов проверьте также, что поля действительно приватные.
from employee import Employee, TypeError
import unittest

class TestEmloyee(unittest.TestCase):
    def test_salary(self):
        with self.assertRaises(TypeError):
            emp = Employee("Valerii", "manager", '44')
            emp.set_salary('2')


    def test_name(self):
        with self.assertRaises(TypeError):
            emp = Employee('Olga', "manager", 1000)
            emp.set_name(10)

    def test_att_private(self):
        emp = Employee('Olga', "manager", 100)
        assert emp._Employee__salary == 100








if __name__ == "__main__":
    unittest.main()

