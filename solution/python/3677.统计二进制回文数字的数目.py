"""3677. 统计二进制回文数字的数目"""


class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1
        bits = bin(n)[2:]
        length = len(bits)
        answer = 1
        for size in range(1, length):
            answer += 1 if size == 1 else 1 << ((size - 1) // 2)
        half = (length + 1) // 2
        prefix = int(bits[:half], 2)
        first = 1 << (half - 1)
        candidate = bits[:half] + bits[: length // 2][::-1]
        answer += prefix - first + 1
        if int(candidate, 2) > n:
            answer -= 1
        return answer


if __name__ == "__main__":
    test_cases = [((9,), 6), ((0,), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countBinaryPalindromes(*args) == expected
