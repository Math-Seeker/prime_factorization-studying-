from my_library import primality_test, primality_test_easy, modular_fast_power, my_gcd, my_ec_mod_n
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
    while True:
        b = randint[2, n - 1]
        c = -7 - 2 * b  # y^2 = x^3 + bx + c, P(2, 1)を固定
        gcd = my_gcd(4 * b * b * b + 27 * c * c, n)
        if gcd == n:
            continue
        if gcd > 1:
            return [gcd, n // gcd]
        
        ec = my_ec_mod_n(b, c, n)
        # ここからkPの計算、繰り返し2乗法


# 入力など
print("Prime Factorization")
s = input("Please Enter A Number: ")
n = int(s.replace(',', ''))
Factors = [n]
PrimeFactors = {}

# 素因数分解操作


# 出力
first = True
print(f"{s} = ", end = '')
sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
for p in sorted(PrimeFactors):
    if first:
        first = False
    else:
        print(" x ", end = '')

    if PrimeFactors[p] == 1:
        print(f"{p}", end = '')
    else:
        print(f"{p}{str(PrimeFactors[p]).translate(sup)}", end = '')