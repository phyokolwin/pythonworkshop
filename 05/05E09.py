
import random

class Pet():
    def __init__(self, height):
        self.height = height

        is_human = False

        @classmethod
        def owned_by_smith_family(cls):
            return 'smith' in cls.owner

        @classmethod
        def create_random_height_pet(cls):
            height = random.randrange(0, 100)
            return cls(height)

my_pet = Pet(50)
for i in range(5):
    pet = my_pet.create_random_height_pet()
    print(my_pet.height)
