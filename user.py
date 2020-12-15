# DONE-1: Add Supervisor class Here

class Supervisor:

    def __init__(self, username, password, phone_number):
        """
        initiate Supervisor class
        :param username: a string for username
        :param password: a string for password
        :param phone_number: a string for phone number
        """
        self.username = username
        self.password = password
        self.phone_number = phone_number

# DONE-1: Add .sample() classmethod for Supervisor which returns an instance:
    @classmethod
    def sample(cls):
        """
        a class method to create a sample from Supervisor class
        :return: a object from Supervisor class
        """
        result = {
            'name': 'pemidi',
            'password': '12345',
            'phone_number': '09121231234'
        }
        return cls(**result)


# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
