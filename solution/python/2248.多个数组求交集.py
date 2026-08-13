"""2248. 多个数组求交集"""


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        common = set(nums[0])
        for values in nums[1:]:
            common &= set(values)
        return sorted(common)

if __name__ == "__main__":
    assert Solution().intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]) == [3,4]
