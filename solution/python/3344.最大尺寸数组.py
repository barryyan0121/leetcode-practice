class Solution:
    def maxSizedArray(self, s: int) -> int:
        def total(n: int) -> int:
            pairs = 0
            for bit in range(n.bit_length()):
                zero = (n >> (bit + 1)) * (1 << bit) + min(
                    n & ((1 << (bit + 1)) - 1), 1 << bit
                )
                pairs += n * n - zero * zero
            return n * (n - 1) // 2 * pairs

        left, right = 1, 2
        while total(right) <= s:
            right *= 2
        while left < right:
            middle = (left + right + 1) // 2
            if total(middle) <= s:
                left = middle
            else:
                right = middle - 1
        return left


if __name__ == "__main__":
    test_cases = [
        ((10,), 2),
        ((0,), 1),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().maxSizedArray(s) == expected
