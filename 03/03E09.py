
def get_second_element(mylist):
    if len(mylist) > 1:
        return mylist[1]
    else:
        return 'List was too small'

get_second_element([1, 2, 3])

get_second_element([1])
