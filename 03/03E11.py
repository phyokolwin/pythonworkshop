def list_product(my_list): 
    result = 1
    for number in my_list: 
         result = result * number
    return result

print(list_product([2, 3]))
print(list_product([2, 10, 15]))

# from multiply import list_product
list_product([-1, 2, 3])
