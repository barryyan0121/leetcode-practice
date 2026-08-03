class Solution:
    def minEnd(self, n: int, x: int) -> int:
        remaining = n - 1
        answer = x
        bit = 0
        while remaining:
            if not (x >> bit) & 1:
                if remaining & 1:
                    answer |= 1 << bit
                remaining >>= 1
            bit += 1
        return answer


if __name__ == "__main__":
    test_cases = [(3, 4, 6), (2, 7, 15), (4, 2, 7)]
    for _, (n, x, expected) in enumerate(test_cases):
        assert Solution().minEnd(n, x) == expected
