def lesser_of_two_evens(a,b):
    """
    docstring
    """
    print("hi")
    if a%2 == 0 and b%2==0:
        print("Both even numbers, will return smaller value.")
        # if a < b: return a
        # else: return b
        return min(a,b)
    else:
        print("One or both of the numbers are not even, returning bigger value.")
        # if a > b: return a
        # else: return b
        return max(a,b)
    pass

print("lesser_of_two_evens(2,4) is {}".format(lesser_of_two_evens(2,4)))
print("lesser_of_two_evens(4,5) is {}".format(lesser_of_two_evens(4,5)))
