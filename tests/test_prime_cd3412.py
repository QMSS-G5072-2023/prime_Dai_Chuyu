import sys
sys.path.insert(0, '/Users/dcy/Documents/MDS/prime_cd3412/prime_cd3412/src/prime_cd3412')
from prime_cd3412 import *

def test_is_prime():
    actual = []
    example = [2,7,8,9]
    expected = [True, True, False, False] # expected return from the function
    for number in example:
      actual_value = is_prime(number)
      actual.append(actual_value)
    assert actual == expected, f"For {example}, expected {expected}, but got {actual}"
