# Очевидно, что обязательно стоит протестировать выбрасывание
# исключения в validate_user.
from user import User, UsernameTooShortException, PasswordTooWeakException
import unittest

class TestUser(unittest.TestCase):
    def test_user_login(self):
        with self.assertRaises(UsernameTooShortException):
            user = User(' ', '1aaa7845')
            user.validate_user()

    def test_user_password(self):
        with self.assertRaises(PasswordTooWeakException):
            user = User('klj7k', 'a')
            user.validate_user()

    def test_users_log(self):
        user2 = User('klj7k', '1aaa7845')
        assert len(user2.username) >= 5
        print(f'Данный логин {user2.username} прошел валидацию')

    def test_users_pas(self):
        user2 = User('klj7k', '1aaa7845')
        assert len(user2.password) >= 8
        print(f'Пароль корректный {user2.password}')





if __name__ == "__main__":
    unittest.main()