
class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def __str__(self):
        return self.name


chad = Country(name='Chad')
print(chad)

class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def __str__(self):
        label = self.name
        if self.population:
            label = '%s, population: %s' % (label, self.population)
        if self.size_kmsq:
            label = '%s, size_kmsq: %s' % (label, self.size_kmsq)
        return label


chad = Country(name='Chad', population=100)
print(chad)
