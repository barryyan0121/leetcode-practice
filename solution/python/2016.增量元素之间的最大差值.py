"""2016. 增量元素之间的最大差值"""


class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        smallest = nums[0]
        answer = -1
        for value in nums[1:]:
            answer = max(answer, value - smallest)
            smallest = min(smallest, value)
        return answer if answer > 0 else -1


if __name__ == "__main__":
    test_cases = [(([7, 1, 5, 4],), 4), (([9, 4, 3, 2],), -1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximumDifference(*args) == expected
