# DONE-1: Add Supervisor class Here
from lib import Root


class Supervisor(Root):
    supervisor_list = []

    def __init__(self, username, password, phone_number, *args, **kwargs):
        """
        initiate Supervisor class
        :param username: a string for username
        :param password: a string for password
        :param phone_number: a string for phone number
        """
        self.username = username
        self.password = password
        self.phone_number = phone_number
        Supervisor.supervisor_list.append(self)
        super().__init__(*args, **kwargs)

# DONE-1: Add .sample() classmethod for Supervisor which returns an instance:
    @classmethod
    def sample(cls, username='pemidi',
               password='12345',
               phone_number='09121231234'):
        """
        a class method to create a sample from Supervisor class
        :return: a object from Supervisor class
        """
        return cls(username=username,
                   password=password,
                   phone_number=phone_number)


# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
