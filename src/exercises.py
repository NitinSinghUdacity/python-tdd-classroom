def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    input_list=input_list[::-1]
    return input_list

def count_digits(number):
    """
    Return count of digits
    """
    count=0
    while number:
        count+=1
        number=number//10
    return count
