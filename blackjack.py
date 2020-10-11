def blackjack(a,b,c):
    """
    docstring
    """
    input_array = [a,b,c]
    sum_input_array = sum(input_array)
    
    if sum_input_array <= 21:
        return sum_input_array
    elif 11 in input_array and sum_input_array <= 31:
        return sum_input_array-10
    else:
        return "BUST"


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print(blackjack(9,6,9))

