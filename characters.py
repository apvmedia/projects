import random


class Thief:
    sneaky = True
    # methods operate on an instance of the class not the class, that's why we must pass in an object

    def __init__(self, name, sneaky=True, **kwargs):
        self.name = name
        self.sneaky = sneaky

        for key, value in kwargs.items():
            setattr(self, key, value)

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10


kenneth = Thief("Ken", False)
# print(kenneth.pickpocket())
# print(Thief.pickpocket(kenneth))
# kenneth.sneaky = False
# print(kenneth.pickpocket())
# print(Thief.pickpocket(kenneth))
