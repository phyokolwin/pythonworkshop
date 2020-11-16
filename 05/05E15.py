
import datetime
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Baby(Person):
    def speak(self):
        print('Blah blah blah')

class Adult(Person):
    def speak(self):
        print('Hello, my name is %s' % self.first_name)


class Calendar():
    def book_appointment(self, date):
        print('Booking appointment for date %s' % date)


class OrganizedAdult(Adult, Calendar):
    pass

class OrganizedBaby(Baby, Calendar):
    pass


andres = OrganizedAdult('Andres', 'Gomez')
boris = OrganizedBaby('Boris', 'Bumblebutton')

andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2018,1,1))


class OrganizedBaby(Baby, Calendar):
    def book_appointment(self, date):
        print('Note that you are booking an appointment with a baby.')
        super().book_appointment(date)


boris = OrganizedBaby('Boris', 'Bumblebutton')
boris.book_appointment(datetime.date(2018,1,1))
