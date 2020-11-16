
class Person() :
    def __int__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.first_name)


customer = Person('Mary', 'Lou')
customer.full_name


if __name__=='__main__':
    customer.full_name = 'Mary Schmidt'
