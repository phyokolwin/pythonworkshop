
class Pet() :
    def __init__(self, height):
        self.height = height

    is_human = False
    owner = 'Michael Smith'

    def is_tall(self):
        return self.height >= 50

bowser = Pet(40)
bowser.is_tall()

bowsey = Pet(60)
bowsey.is_tall()
