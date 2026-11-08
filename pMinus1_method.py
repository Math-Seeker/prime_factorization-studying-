from my_library import primality_test, primality_test_easy, modular_fast_power, my_gcd

# 関数定義
def Pollard_Method(n : int) -> list[int]:
    if primality_test_easy(n):
        if primality_test(n):
            return [n]
    a = 2
    k, k0 = 2520, 9  # 2520 = LCM[1,2,3,4,5,6,7,8,9]
    while a * a <= n:
        gcd1 = my_gcd(a, n)
        if gcd1 > 1:
            return [n // gcd1, gcd1]
        else:
            a_k = modular_fast_power(a, k ,n)
            gcd2 = my_gcd(a_k - 1, n)
            if gcd2 == 1:
                for i in range(k0):
                    k0 += 1
                    k = k // my_gcd(k, k0) * k0
            elif gcd2 == n:
                a += 1
            else:
                return [n // gcd2, gcd2]
    return [n]

# 入力など
print("Prime Factorization")
s = input("Please Enter A Number: ")
n = int(s.replace(',', ''))
Factors = [n]
PrimeFactors = {}

# 素因数分解操作
while Factors:
    n = Factors.pop()
    fac = Pollard_Method(n)
    if len(fac) == 1:
        PrimeFactors[n] = PrimeFactors.get(n, 0) + 1
    else:
        Factors += fac

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