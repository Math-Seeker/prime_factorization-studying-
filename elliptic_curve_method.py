from my_library import primality_test, primality_test_easy, my_gcd, my_ec_mod_n
from random import randint

# 関数定義
def ec_method(n: int) -> list:
    """入力nは整数, n > 1"""
    if primality_test_easy(n):
        if primality_test(n):
            return [1, n]
    if n % 2 == 0:
        return [2, n // 2]
    if n % 3 == 0:
        return [3, n // 3]

    k, k0 = 121645100408832000, 19  # 121645100408832000 = 19!
    while True:
        P = (randint(1, n - 1), randint(1, n - 1))
        b = randint(1, n - 1)
        c = (P[1] * P[1] - (P[0] * P[0] - b) * P[0]) % n  # y^2 = x^3 + bx + c
        gcd = my_gcd(4 * b * b * b + 27 * c * c, n)
        if gcd == n:
            continue
        if gcd > 1:
            return [gcd, n // gcd]
        
        ec = my_ec_mod_n(b, c, n)
        # ここからkPの計算、繰り返し2乗法
        kP = (None, None)
        k1 = k
        while k1 != 0:
            if k1 % 2 == 1:
                kP = ec.add(kP, P)
                if kP[0] is None:
                    if kP[1] is None:
                        break
                    else:
                        return [kP[1], n // kP[1]]
            P = ec.add(P, P)
            if P[0] is None:
                if P[1] is None:
                    break
                else:
                    return [P[1], n // P[1]]
            k1 //= 2

        for i in range(k0 // 6):
            k0 += 1
            k *= k0


# 入力など
print("Prime Factorization")
s = input("Please Enter A Number: ")
n = int(s.replace(',', ''))
Factors = {n : 1}
PrimeFactors = {}

# 素因数分解操作
while Factors:
    n, power = Factors.popitem()
    fac1, fac2 = ec_method(n)
    if fac1 == 1:
        PrimeFactors[fac2] = PrimeFactors.get(fac2, 0) + power
    else:
        Factors[fac1] = Factors.get(fac1, 0) + power
        Factors[fac2] = Factors.get(fac2, 0) + power

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