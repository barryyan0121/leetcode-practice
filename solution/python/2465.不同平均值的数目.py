"""2465. 不同平均值的数目"""


class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        return len({nums[left] + nums[~left] for left in range(len(nums) // 2)})

if __name__ == "__main__":
    assert Solution().distinctAverages([4,1,4,0,3,5]) == 2
