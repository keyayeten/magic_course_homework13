import unittest
from angle import Angle

class TestAngle(unittest.TestCase):
    def setUp(self):
        self.angle1 = Angle(50)
        self.angle2 = Angle(50)
        self.expecred = Angle(100)

        self.angle3 = Angle(150)
        self.angle4 = Angle(100)
        self.expecred2 = Angle(50)


    def test_add_angle(self):
        res1 = self.angle1 + self.angle2
        self.assertEquals(res1, self.expecred, "No")
        print(f'Угол равен {self.expecred}')

    def test_sub_angle(self):
        res1 = self.angle3 - self.angle4
        self.assertEquals(res1, self.expecred2, "No")
        print(f'Угол равен {self.expecred2}')



if __name__ == "__main__":
    unittest.main()