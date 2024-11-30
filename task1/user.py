# Создайте класс User с полями username и password.
# Реализуйте собственные исключения:

# UsernameTooShortException — выбрасывается,
# если длина username меньше 5 символов.

# PasswordTooWeakException — выбрасывается,
# если пароль не соответствует заданным требованиям
# (например, меньше 8 символов или не содержит цифр).

# Создайте метод validate_user(), который проверяет корректность
# username и password и выбрасывает исключения при необходимости.

class UsernameTooShortException(Exception):
    def __str__(self):
        return f'Не корректный username'


class PasswordTooWeakException(Exception):
    def __str__(self):
        return f'Не корректный password'
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_user(self):
        if len(self.username) < 5:
            raise UsernameTooShortException
        if not self.password.isdigit() and len(self.password) < 8:
            raise PasswordTooWeakException
        return self.username, self.password

    def __str__(self):
        return f'{self.username, self.password}'


# user1 = User('klj', '1a')
# print(user1.validate_user())
# user2 = User('klj7k', '1aaa7845')
# print(user2.validate_user())
# user3 = User(' ', '1aaa7845')
# print(user3.validate_user())
# user4 = User('klj7k', 'a')
# print(user4.validate_user())
