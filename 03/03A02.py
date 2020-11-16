def format_customer(first, last, location=None):
    full_name = '%s %s' % (first, last)
    if location:
        return '%s (%s)' % (full_name, location)
    else:
        return full_name

from customer import format_customer
format_customer('John', 'Smith', location='California')
format_customer('Mareike', 'Schmidt')
