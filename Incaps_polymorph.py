class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_e):
        if  '@' in new_e and new_e.count('@') == 1 and  new_e.find('@') < new_e.find('.'):
            self.__email = new_e
        else: print('Ошибочная почта')


k = UserMail('belosnezhka227', 'prince@wait.you')
# print(k.get_email())
k.set_email([1, 2, 3])
k.set_email('prince@wait@.you')
k.set_email('fafa@mail.ru')
print(k.get_email())