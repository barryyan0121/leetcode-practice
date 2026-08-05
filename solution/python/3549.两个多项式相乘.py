"""3549. 两个多项式相乘"""

from cmath import exp, pi


class Solution:
    def multiply(self, poly1: list[int], poly2: list[int]) -> list[int]:
        n = 1
        size = len(poly1) + len(poly2) - 1
        while n < size:
            n <<= 1

        def fft(values, inverse=False):
            j = 0
            for i in range(1, n):
                bit = n >> 1
                while j & bit:
                    j ^= bit
                    bit >>= 1
                j ^= bit
                if i < j:
                    values[i], values[j] = values[j], values[i]
            length = 2
            sign = 1 if inverse else -1
            while length <= n:
                root = exp(sign * 2j * pi / length)
                for start in range(0, n, length):
                    factor = 1
                    half = length // 2
                    for i in range(start, start + half):
                        even, odd = values[i], values[i + half] * factor
                        values[i], values[i + half] = even + odd, even - odd
                        factor *= root
                length <<= 1
            if inverse:
                for i in range(n):
                    values[i] /= n

        first = list(map(complex, poly1)) + [0j] * (n - len(poly1))
        second = list(map(complex, poly2)) + [0j] * (n - len(poly2))
        fft(first)
        fft(second)
        for i in range(n):
            first[i] *= second[i]
        fft(first, True)
        return [round(first[i].real) for i in range(size)]


if __name__ == "__main__":
    test_cases = [
        (([3, 2, 5], [1, 4]), [3, 14, 13, 20]),
        (([1, 0, -2], [-1]), [-1, 0, 2]),
    ]
    for _, ((poly1, poly2), expected) in enumerate(test_cases):
        assert Solution().multiply(poly1, poly2) == expected
