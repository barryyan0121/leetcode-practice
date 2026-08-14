"""3397. 执行操作后不同元素的最大数量"""


class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        answer = 0
        previous = -(10**30)
        for value in sorted(nums):
            candidate = max(previous + 1, value - k)
            if candidate <= value + k:
                answer += 1
                previous = candidate
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 2, 3, 3, 4], 2), 6),
        (([4, 4, 4, 4], 1), 3),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxDistinctElements(*args) == expected
