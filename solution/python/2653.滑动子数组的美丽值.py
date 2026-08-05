"""2653. 滑动子数组的美丽值"""


class Solution:
    def getSubarrayBeauty(self, nums: list[int], k: int, x: int) -> list[int]:
        answer = []
        for left in range(len(nums) - k + 1):
            negatives = sorted(value for value in nums[left : left + k] if value < 0)
            answer.append(negatives[x - 1] if len(negatives) >= x else 0)
        return answer


if __name__ == "__main__":
    test_cases = [(([1, -1, -3, -2, 3], 3, 2), [-1, -2, -2])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().getSubarrayBeauty(*args) == expected
