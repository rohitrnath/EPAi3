def docstringLenChecker( arg_minimum_length = 50):
    """
    This function is used to initialise a closure which can check
    if the docstring length(character count) of the function passed to 
    the closure object is minimum of 'arg_minimum_length' value(default 50) or not.

    docstringLenChecker:
        input:  1. integer
                arg_minimum_length: Argument contains the count of 
                minimum check. default value is 50.
        output: function docstringLenCheck_inner function object
    """

    def docstringLenCheck_inner( arg_func):
        """
        This function takes a function as input and compare the docstring character count
        with the free variable arg_minimum_length and return true or false.

        docstringLenCheck_inner:
            input: a function is taken as input argument
            output: boolean
                    'true' if the docstring length is less than arg_minimum_length
                    'false' if the docstring length is less than arg_minimum_length
        """
        nonlocal arg_minimum_length
        if len(arg_func.__doc__) >= arg_minimum_length:
            return True
        else:
            return False
    return docstringLenCheck_inner


def fibonacci_generator():
    """
    Function to generate fibonacci sequence.
    This function initialise a closure which can generate the 
    fibonacci number in each function call. It starts from 
    second fibonacci number.

    fibonacci_generator:
        Input: None
        Output: Function fibonacci_generator_inner() object
    """
    first_fibonacci = 0  #first fibonacci number
    second_fibonacci = 1 #second fibonacci number

    def fibonacci_generator_inner():
        """
        This function can generate the next fibanocci number based on
        the sum of previous two numbers.

        fibonacci_generator_inner:
            Input: None
            Output: (n-2)th fibonacci number. n is the number of times
                    the function object called. 
        """
        nonlocal first_fibonacci, second_fibonacci

        first_fibonacci, second_fibonacci = second_fibonacci, first_fibonacci # make the current second fibonacci as next first fibonacci
        
        second_fibonacci = first_fibonacci+second_fibonacci # Finding the new fibonacci and assigning it to second fibonacci variable for next iteration.

        return second_fibonacci
    return fibonacci_generator_inner