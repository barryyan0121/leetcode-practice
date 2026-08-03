class Solution:
    def minOperations(self, k: int) -> int:
        answer = k - 1
        for value in range(1, k + 1):
            copies = (k + value - 1) // value
            answer = min(answer, value - 1 + copies - 1)
        return answer


if __name__ == "__main__":
    test_cases = [(11, 5), (1, 0), (10, 5)]
    for _, (k, expected) in enumerate(test_cases):
        assert Solution().minOperations(k) == expected
