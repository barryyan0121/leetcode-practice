"""2860. 让所有学生保持开心的分组方法数"""


class Solution:
    def countWays(self, nums: list[int]) -> int:
        nums.sort()
        answer = 0
        for group_size in range(len(nums) + 1):
            if (group_size == 0 or nums[group_size - 1] < group_size) and (
                group_size == len(nums) or nums[group_size] > group_size
            ):
                answer += 1
        return answer


if __name__ == "__main__":
    assert Solution().countWays([1, 1]) == 2
