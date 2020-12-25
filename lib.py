# DONE-3: Create Manager class which has _class attr and search() method
from abc import ABC


class Manager:

    def __init__(self, _class=None):
        self._class = _class

    def __str__(self):
        return f"Manager {self._class}"

    def search(self):
        pass


class Root(ABC):
    _id = 0
    objects_list = None
    manager = None

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        # self.store(self)
        self.set_manager()
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)





# DONE-3: Implement complete search method functionality in the way you prefer
# DONE-3: `_class` attr in manager is type of composite class
# DONE-3: Add Root class and set manager class_attr None in it
# DONE-3: Add set_manager() method to the Root which set type of self to the
#       `_class` attr of instance manager

# TODO-3: Change sample() method all over your code as follows:

#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls, name='ali', number=10):
#             return cls(name=name, number=number)
# DONE-3: Add <class-name-lowercase>_list class_attr to the all classes except
#       Manager() and Root() classes
