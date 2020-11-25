def division(num):
    divided = int(num)
    # AssertionError: divided value is 0!
    assert divided != 0, 'divided value is 0!'
    return 10 / divided


division(0)
