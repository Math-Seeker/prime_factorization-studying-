# 関数定義
def my_gcd(a : int, b : int):  # my_gcd(a, 0) = a; my_gcd(0, b) = b
    while b:
        c = a % b
        a = b
        b = c
    return a

def modular_fast_power(a : int, k : int, n : int):  # return (a ^ k) mod n
    res = 1
    while k:
        nonzero = k % 2
        k //= 2
        if nonzero:
            res *= a
            res %= n
        a = (a * a) % n
    return res


def primality_test_easy(n : int) -> bool:  # 2 ^ (p - 1) = 1 (mod p), Falseは本当にFalse, Trueは間違う可能性がある
    if n == 2:
        return True
    x = modular_fast_power(2, n - 1, n)
    if x != 1:
        return False
    else:
        return True


base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
# Miller-Rabin法の底、n < 3,317,044,064,679,887,385,961,981のnを正しく判定できる。
# =の場合は合成数だが、素数と判定してしまう(解決策：底を増やす)
def primality_test(n : int) -> bool:  # 素数判定、Miller–Rabin法
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        m = n - 1
        power = 0
        while m % 2 == 0:
            power += 1
            m //= 2

        for b in base:
            if n == b:
                break
            b = modular_fast_power(b, m, n)
            if b != 1 and b != n - 1:
                for i in range(power - 1):
                    b = (b * b) % n
                    if b == n - 1:
                        break
                else:
                    return False

        return True

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