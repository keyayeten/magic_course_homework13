# Создайте класс Angle, который хранит значение угла в градусах.
# Реализуйте __add__ и __sub__, чтобы складывать и вычитать углы.


class Angle:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        res = self.a + other.a
        return Angle(res) if res < 180 else Angle(0)


    def __sub__(self, other):
        yg = (self.a - other.a)
        return Angle(abs(yg))


    def __repr__(self):
        return f"Angle({self.a})"

    def __eq__(self, other):
        if isinstance(other, Angle):
            return self.a == other.a
        return False

# ygol = Angle(130)
# ygol2 = Angle(50)
# ygol3 = Angle(10)
# print(ygol + ygol2)
# print(ygol2 - ygol)
# print(ygol2 + ygol3)
