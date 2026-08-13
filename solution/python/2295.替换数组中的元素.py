"""2295. 替换数组中的元素"""


class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        positions = {value: i for i, value in enumerate(nums)}
        for old, new in operations:
            index = positions.pop(old)
            positions[new] = index
            nums[index] = new
        return nums

if __name__ == "__main__":
    assert Solution().arrayChange([1,2,4,6], [[1,3],[4,7],[6,1]]) == [3,2,7,1]
