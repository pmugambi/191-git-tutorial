def square(numbers):
    """
    This fucntion computes squares of numbers in a list
    :param numbers: a list of numbers
    :return: a list of the squares of the numbers passed in the input
    """
    try:
        return [x * x for x in numbers]
    except Exception as e:
        print("there was an issue, computing the square of the passed numbers. "
              "Input should be a list of real numbers. The error messages returned is " + str(e))


if __name__ == '__main__':
    print("Squaring characters. Bad input, should fail. See returned error message.")
    numbers = ['a', 14, '-c']  # this should fail to compute squares. bad input
    p = square(numbers)
    print("Squaring real numbers. Good input, should succeed. See returned success confirmation")
    numbers = [1, 0.5, 0, 90, -2.6, 0.00005, -0.001]  # real numbers only. squares should work
    q = square(numbers)
    print("success: squares are :", q)
