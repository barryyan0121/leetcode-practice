"""2939. 最大异或乘积"""


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        modulo = 10**9 + 7
        for bit in range(n - 1, -1, -1):
            mask = 1 << bit
            a_bit, b_bit = a & mask, b & mask
            if a_bit == b_bit:
                if not a_bit:
                    a |= mask
                    b |= mask
            elif a < b:
                a |= mask
                b &= ~mask
            else:
                a &= ~mask
                b |= mask
        return (a % modulo) * (b % modulo) % modulo


if __name__ == "__main__":
    assert Solution().maximumXorProduct(12, 5, 4) == 98
