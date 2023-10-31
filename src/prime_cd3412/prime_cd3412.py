import math

def is_prime(n):
    """
    Check if the input number is a prime number.

    Parameters
    ----------
    n: any real number

    Returns
    -------
    Boolean value
       True: n is a prime number 
       False: n is not a prime number

    Examples
    --------
    >>> n = 7
    >>> is_prime(n)
    True

    >>> n = 180
    >>> is_prime(n)
    False
    """
     
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True