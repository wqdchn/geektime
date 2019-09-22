# @program: PyDemo
# @description: fib(n)
# @author: wqdong
# @create: 2019-09-22 14:26
import math


class Fib:

    # 递归
    def fib_recur(self, n):
        if n == 0: return 0
        if n == 1: return 1
        return self.fib_recur(n - 1) + self.fib_recur(n - 2)

    # 递推
    def fib_loop(self, n):
        res = [0] * (n + 1)
        res[1] = 1
        for i in range(2, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        return res[n]

    def fib_loop2(self, n):
        a, b = 0, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
        return a

    # 通项公式 f(n) = a1(b1)^n + a2(b2)^n
    # a1 = 1/sqrt(5), b1 = (1+sqrt(5))/2
    # a2 = -1/sqrt(5), b2 = (1-sqrt(5))/2
    def fib_fun(self, n):
        a1 = 1 / math.sqrt(5)
        a2 = -1 / math.sqrt(5)
        b1 = (1 + math.sqrt(5)) / 2
        b2 = (1 - math.sqrt(5)) / 2
        return int(a1 * math.pow(b1, n) + a2 * math.pow(b2, n))

    def fib_fun2(self, n):
        def fib_fun2_pow(a, n):
            if not n:
                return 1
            if n < 0:
                return 1 / fib_fun2_pow(a, -n)
            if n % 2:
                return a * fib_fun2_pow(a, n - 1)
            return fib_fun2_pow(a * a, n / 2)

        a1 = 1 / math.sqrt(5)
        a2 = -1 / math.sqrt(5)
        b1 = (1 + math.sqrt(5)) / 2
        b2 = (1 - math.sqrt(5)) / 2
        return int(a1 * fib_fun2_pow(b1, n) + a2 * fib_fun2_pow(b2, n))

    # 矩阵
    def fib_matrix(self, n):
        import numpy
        return (pow(numpy.matrix([[1, 1], [1, 0]]), (n - 1)) *
                numpy.matrix([[1], [0]]))[0, 0]


f = Fib()
n = 15
print(f.fib_recur(n))

print(f.fib_loop(n))
print(f.fib_loop2(n))

print(f.fib_fun(n))
print(f.fib_fun2(n))

print(f.fib_matrix(n))
