"""1968. 构造元素不等于两相邻元素平均值的数组"""


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        middle = len(nums) // 2
        return [
            value for pair in zip(nums[middle:], nums[:middle]) for value in pair
        ] + nums[middle + len(nums) // 2 :]


if __name__ == "__main__":
    test_cases = [(([1, 2, 3, 4],), [1, 3, 2, 4])]
    for _, (args, expected) in enumerate(test_cases):
        result = Solution().rearrangeArray(*args)
        assert all(
            2 * result[i] != result[i - 1] + result[i + 1]
            for i in range(1, len(result) - 1)
        )
