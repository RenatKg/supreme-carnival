def fizz_buzz(number):
    """
    Function admite 'int'.
        back
        * Fizz if parameter divide to 3
        * buzz if parameter devide to 5
        * FizzBuzz if parameter devide to 3 and 5
    """
    if number <= 0:
        return 'SmallInt'
    if number % 15 == 0:
        return 'FizzBuzz'

    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
