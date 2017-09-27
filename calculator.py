# -----------------------------------------------------------------------------
# Name:        calculator
# Purpose:     CS 152 Python Demo
# -----------------------------------------------------------------------------
"""
Simple Prefix Calculator

Evaluate simple expressions using the prefix notation.
Current version only supports addition of integers and floats.
"""


def comment(operands):
    """
    print 'Comment ignored' if the input '#' at the value of a string
    """
    print('\n' + 'Comment ignored' + '\n')


def divide(operands):
    """
    If operand's length equal to 0, return 0
    If operand's length equal to 1 and that operand is not equal to 0, return 1/operand
    if operand's length equal to 1 and that operand is equal to zero, return error comment
    if operand's length is any other length and not equal to zero (impossible to be negative value), return the
    results of the first operand devide by the second operand and that result then divide the next operand in
    the list and so on...
    """
    result = 0
    if len(operands) == 0:
        result = result
    elif len(operands) == 1 and get_value(operands[0]) != 0:
        result = 1 / get_value(operands[0])
    elif len(operands) == 1 and get_value(operands[0]) == 0:
        result == error("non zero operand", get_value(operands[0]))
    else:
        result = get_value(operands[0])

        for each_operand in operands[1:]:
            each_value = get_value(each_operand)
            if each_value is not None and each_value != 0:
                result /= each_value
            elif each_value is not None and each_value == 0:
                result == error("non zero operand", each_value)
            else:
                return
    return result


def multiply(operands):
    """
    If operand's length equal to 0, return 0
    If operand's length equal to 1 , return 1/operand
    if operand's length equal to greater than 1, return multiplication of all the operand's values
    """
    result = 0
    if len(operands) == 0:
        result = result
    elif len(operands) == 1:
        result = 1 * get_value(operands[0])
    elif len(operands) > 1:
        result = get_value(operands[0])

        for each_operand in operands[1:]:
            each_value = get_value(each_operand)
            if each_value is not None:
                result *= each_value
            else:
                return
    return result


def subtract(operands):
    """
        If operand's length equal to 0, return 0
        If operand's length equal to 1 , return 0 - (first operand's value)
        if operand's length equal to greater than 1, return subtraction of all the operand's values
    """
    result = 0
    if len(operands) == 0:
        result = result
    elif len(operands) == 1:
        result = 0 - get_value(operands[0])
    elif len(operands) > 1:
        result = get_value(operands[0])

        for each_operand in operands[1:]:
            each_value = get_value(each_operand)
            if each_value is not None:
                result -= each_value
            else:
                return
    return result


def add(operands):

    """
    Compute the sum of the operands specified if they are all numbers.
    If any operand is not a valid number, the function returns None.
    :param operands: list of strings
    :return: (int or float) the sum of the operands specified if all of them
        are valid numbers or None if an invalid number is encountered.

    """
    result = 0
    for each_operand in operands:
        each_value = get_value(each_operand)  # Get the corresponding number.
        if each_value is not None:  # Each_operand is a valid number, add it.
            result += each_value
        else:    # There is an error, return None.
            return
    return result


# Dictionary mapping supported symbols to functions.
# The functions must be defined above.


SUPPORTED_OPERATORS = {'+': add, '-': subtract, '*': multiply, '/': divide, '#': comment}
SUPPORTED_SYMBOLS = sorted(SUPPORTED_OPERATORS.keys())


def command(expression):
    """
    Evaluate a single expression and print the result.
    :param expression: (string) simple expression in prefix notation
    :return: None
    """
    if not expression:
        return
    result = None
    # Split the expression into a list of words (tokens).
    tokens = expression.split()
    operator = tokens[0]  # in prefix notation, the operator comes first
    operands = tokens[1:]
    if operator in SUPPORTED_OPERATORS:
        function_name = SUPPORTED_OPERATORS[operator]
        result = function_name(operands)
    else:
        expected_operators = ' or '.join(SUPPORTED_SYMBOLS)
        error(expected_operators, operator)
    if result is not None:
        print(result)


def get_value(a_string):
    """
    Convert a string to a number (integer or float).
    If the given string is not a valid number, the function returns None.

    :param a_string(str)
    :return: (int or float) the corresponding number
    """
    try:
        # First try to convert the string to an integer.
        value = int(a_string)
    except ValueError:  # Not a valid integer
        try:
            # Try to convert the string to a float
            value = float(a_string)
        except ValueError:
            error('number', a_string)
            return
    return value


def error(expected, error):
    """
    Print an error message when an unexpected token is encountered.
    :param expected: (string) supported symbols or 'number' or anything else...
    :param error: (string) the actual token encountered
    :return: None
    """
    print("Error:  expected {}, got {}".format(expected, error))
    print('Please enter a valid expression in prefix notation or q to quit')


def main():
    more_input = True
    while more_input:
        expression = input("CS 152 Calculator >>>")
        if expression == 'q':
            more_input = False
            print('Exiting the CS 152 Calculator')
        else:
            command(expression)


if __name__ == '__main__':
    main()