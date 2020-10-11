def summer_of_69(num_array):
    """
    docstring
    """
    total = 0
    add = True

    for num in num_array:
        while add:
            if num!=6:
                total+=num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add=True
                break
    return total

print(summer_of_69([1,3,5]))
print(summer_of_69([4,5,6,7,8,9]))
print(summer_of_69([2,1,6,9,11]))
print(summer_of_69([4,5,6,7,8,9,10]))
print(summer_of_69([4,5,6,7,8,10]))
