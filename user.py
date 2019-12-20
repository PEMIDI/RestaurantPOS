# TODO-1: Add Supervisor class Here
class Supervisor:
    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number

# TODO-1: Add .sample() classmethod for Supervisor which returns an instance:
    @classmethod
    def sample(cls):
        return cls(username='ja4ari', password='123',
                   phone_number='09377359595')
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
