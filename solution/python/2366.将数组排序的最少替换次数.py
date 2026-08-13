"""2366. 将数组排序的最少替换次数"""


class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        answer = 0
        limit = nums[-1]
        for value in reversed(nums[:-1]):
            parts = (value + limit - 1) // limit
            answer += parts - 1
            limit = value // parts
        return answer

if __name__ == "__main__":
    assert Solution().minimumReplacement([3,9,3]) == 2
