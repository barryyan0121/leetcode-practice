from math import gcd


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(left: int, right: int) -> int:
            return left // gcd(left, right) * right

        ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
        abc = lcm(ab, c)
        low, high = 1, min(a, b, c) * n
        while low < high:
            middle = (low + high) // 2
            count = (
                middle // a
                + middle // b
                + middle // c
                - middle // ab
                - middle // ac
                - middle // bc
                + middle // abc
            )
            if count >= n:
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [(3, 2, 3, 5, 4), (4, 2, 3, 4, 6)]
    for _, (n, a, b, c, expected) in enumerate(test_cases):
        assert Solution().nthUglyNumber(n, a, b, c) == expected
