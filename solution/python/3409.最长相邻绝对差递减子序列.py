class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        limit = 300
        best = [[0] * (limit + 1) for _ in range(limit + 1)]
        seen = [False] * (limit + 1)
        answer = 1
        for value in nums:
            candidates = [0] * (limit + 1)
            for previous in range(1, limit + 1):
                if seen[previous]:
                    difference = abs(value - previous)
                    candidates[difference] = max(
                        candidates[difference], best[previous][difference] or 1
                    )
            for difference in range(limit - 1, -1, -1):
                candidates[difference] = max(
                    candidates[difference], candidates[difference + 1]
                )
            for difference in range(limit + 1):
                best[value][difference] = max(
                    best[value][difference], candidates[difference] + 1
                )
                answer = max(answer, best[value][difference])
            seen[value] = True
        return answer


if __name__ == "__main__":
    test_cases = [
        (([16, 6, 3],), 3),
        (([6, 5, 3, 4, 2, 1],), 4),
        (([10, 20, 10, 19, 10, 20],), 5),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().longestSubsequence(nums) == expected
