from my_library import primality_test, primality_test_easy, modular_fast_power, my_gcd
from random import randint

# 関数定義
def ec_method(n: int) -> list:
    """入力nは整数, n > 1"""
    if primality_test_easy(n):
        if primality_test(n):
            return [n]
    if n % 2 == 0:
        return [2, n // 2]
    if n % 3 == 0:
        return [3, n // 3]

    k, k0 = 12252240, 17  # LCM[1,2,3,...,17] = 12252240
    b = randint[2, n - 1]
    