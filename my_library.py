def my_gcd(a : int, b : int):  # my_gcd(a, 0) = a; my_gcd(0, b) = b
    while b:
        c = a % b
        a = b
        b = c
    return a

def modular_fast_power(a : int, k : int, n : int):
    """return (a ^ k) mod n"""
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
    
def mod_inverse(a : int, n : int) -> tuple:
    """return (True, a^(-1) mod n) or (False, gcd(a, n))"""
    P = []
    N = n
    while a != 0:
        P.append(n // a)
        r = n % a
        n = a
        a = r
    if n == 1:
        P.pop()
        x, y = 1, -P.pop()  # nx + ay = 1の解yを求める
        while P:
            p = P.pop()
            x, y = y, x - p * y
        return (True, y % N)
    else:
        return (False, n)

class my_ec_mod_n:
    """y^2 = x^3 + bx + c (mod n)"""
    def __init__(self, b : int, c : int, n : int):
        self.b = b
        self.c = c
        self.n = n
        self.invertible_2, self.inver_2 = mod_inverse(2, n)
    def add(self, P : tuple, Q : tuple) -> tuple:
        """return (x3, y3) or (None, nの約数), 無限遠点：(None, None)"""
        # gcd(y, n) = n or gcd(x2 - x1, n) = nの時、無限遠点を返す
        x1, y1 = P[0] % self.n, P[1] % self.n
        x2, y2 = Q[0] % self.n, Q[1] % self.n
        if y1 is None:
            return (x2, y2)
        elif y2 is None:
            return (x1, y1)
        
        if x1 == x2 and y1 == y2:
            if not self.invertible_2:
                return (None, 2)
            if y1 == 0:
                return (None, None)
            inver, inver_y1 = mod_inverse(y1, self.n)
            if not inver:
                return (None, inver_y1)
            k = (3 * x1 * x1 + self.b) % self.n * self.inver_2 * inver_y1 % self.n
            x3 = (k * k - 2 * x1) % self.n
            y3 = (k * (x1 - x3) - y1) % self.n
        else:
            x1, y1 = P[0], P[1]
            x2, y2 = Q[0], Q[1]
            x2_minus_x1 = (x2 - x1) % self.n
            if x2_minus_x1 == 0:
                return (None, None)
            inver, inver_x2_minus_x1 = mod_inverse(x2 - x1, self.n)
            if not inver:
                return (None, inver_x2_minus_x1)
            k = (y2 - y1) * inver_x2_minus_x1 % self.n
            x3 = (k * k - x1 - x2) % self.n
            y3 = (k * (x1 - x3) - y1) % self.n

        return (x3, y3)