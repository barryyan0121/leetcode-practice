"""2420. 找到所有好下标"""


class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        nonincreasing = [1] * n
        nondecreasing = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                nonincreasing[i] = nonincreasing[i - 1] + 1
            if nums[i] >= nums[i - 1]:
                nondecreasing[i] = nondecreasing[i - 1] + 1
        return [
            i
            for i in range(k, n - k)
            if nonincreasing[i - 1] >= k and nondecreasing[i + k] >= k
        ]


if __name__ == "__main__":
    test_cases = [(([2, 1, 1, 1, 3, 4, 1], 2), [2, 3])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().goodIndices(*args) == expected
