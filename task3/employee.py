# Создайте класс Employee, который инкапсулирует следующие данные:

# Приватные поля __name, __position, __salary.

# Методы set_name, set_position и set_salary для изменения
# значений этих полей (например, при повышении сотрудника).
# Ограничьте прямой доступ к __salary, добавив проверку,
# чтобы зарплату можно было изменить только через метод, например,
# при повышении. Запрещается устанавливать зарплату ниже текущего значения.

# Метод get_employee_info, который возвращает информацию о сотруднике
# в виде строки.
class TypeError(Exception):
    pass

class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    def set_position(self, position):
        if not isinstance(position, str):
            raise TypeError
        self.__position = position


    def set_salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError
        if new_salary < self.__salary:
            self.__salary = self.__salary
        self.__salary = new_salary

    def get_employee_info(self):
        return f'{self.__name} {self.__position} его зарплата {self.__salary}'

# a = Employee("Valerii", "manager", 10000)
# print(a.get_employee_info())
# # print(a.set_name())
# a.set_position('Старший менеждер')
# a.set_salary(200000)
# print(a.get_employee_info())
#
#
# a = Employee("Mark", "doktor", 100)
# print(a.get_employee_info())
# # print(a.set_name())
# a.set_position("doktor")
# a.set_salary(2)
# print(a.get_employee_info())