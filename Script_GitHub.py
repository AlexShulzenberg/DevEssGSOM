# Func_mod

def find_two_smallest(lissst):
    """ 
    Receives a list of integers as a parameter and returns (not prints! returns!) two smallest list values
    """
    list_copy = lissst
    a = list_copy.pop(list_copy.index(min(list_copy)))
    b = list_copy.pop(list_copy.index(min(list_copy)))
    return(a, b)

# list_mod # The module defines 3-4 lists of integers.

l1 = [1, 2, 3, 4, 5, 0]
l2 = [1, 123, 2, -124, 12]
l3 = [12345, 125790, 98776, 987, -12345566]
l4 = l1 + l2 + l3

# Script

txt1 = f'In the first list two smallest nums are: {func_mod.find_two_smallest(list_mod.l1)}'
txt2 = f'In the second list two smallest nums are: {func_mod.find_two_smallest(list_mod.l2)}'
txt3 = f'In the third list two smallest nums are: {func_mod.find_two_smallest(list_mod.l3)}'
txt4 = f'In the fourth list two smallest nums are: {func_mod.find_two_smallest(list_mod.l4)}'

result_file = 'result.txt'
file = open(result_file, 'w')
file.write(txt1 + "\n" +
            txt2 + "\n" +
            txt3 + "\n" +
            txt4 + "\n")
file.close()