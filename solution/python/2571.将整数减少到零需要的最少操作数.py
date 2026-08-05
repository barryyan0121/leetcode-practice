"""2571. 将整数减少到零需要的最少操作数"""


class Solution:
    def minOperations(self, n: int) -> int:
        answer = 0
        while n:
            if n & 1:
                answer += 1
                if n & 3 == 3:
                    n += 1
            n >>= 1
        return answer


if __name__ == "__main__":
    test_cases = [((39,), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
