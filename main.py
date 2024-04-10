# Consider explicitly re-raising using 'raise Error from'

# Use the `from` keyword when chaining exceptions

try:
    raise ValueError
except Exception as MyException:
    raise TypeError from MyException