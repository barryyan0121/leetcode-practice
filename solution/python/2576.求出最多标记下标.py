"""2576. 求出最多标记下标"""


class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        nums.sort()
        left, right = 0, (len(nums) + 1) // 2
        answer = 0
        while left < (len(nums) + 1) // 2 and right < len(nums):
            if 2 * nums[left] <= nums[right]:
                answer += 2
                left += 1
            right += 1
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 5, 2, 4],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxNumOfMarkedIndices(*args) == expected
