# This is the implementation for question of Credity
# With regard to the problem of Euler project, the solution must be 2129970655314432
# Kevin Rosales Systems Ing and BI specialist


def first_process(number_iterative):
    '''
    This function get all the values of number 10 ** 9 and to create a new list
    The module operator does nothing but return the rest of the division between the two operands. In the example,
    7/2 would be 3, with 1 remaining, then the module is 1.
    :param number_iterative:
    :return:list
    '''
    custom_list = []
    while number_iterative:
        k = number_iterative % 7
        number_iterative = number_iterative // 7
        custom_list.insert(0, k)
    return custom_list


def process(raw_list):
    '''
    This is the main function that return the result of Pascal triangle
    raw_list[1:] getting the items of right side
    :param raw_list:
    :return: int
    '''
    base = 7
    if not raw_list:
        return 0
    columns = raw_list[0]
    if not columns:
        return process(raw_list[1:])
    if columns < base:
        columns*(1+columns) // 2
    y = base * (1+base) // 2
    # main calculation of function
    step1 = columns*(columns+1) // 2
    step2 = step1 * y ** (len(raw_list)-1)
    step3 = step2 + (columns+1) * process(raw_list[1:])
    return step3


rows_of_pascal = 10 ** 9  # expo number
final_result = process(first_process(rows_of_pascal))
correct_value = 2129970655314432
if correct_value == final_result:
    print('The answer {} is OK'.format(final_result))
else:
    print('The answer {} is wrong. Correct value is {}'.format(final_result, correct_value))

