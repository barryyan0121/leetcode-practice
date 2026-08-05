"""2044. 统计按位或能得到最大值的子集数目"""


class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        target = 0
        for value in nums:
            target |= value
        count = 0

        def search(index: int, value: int) -> None:
            nonlocal count
            if index == len(nums):
                count += value == target
                return
            search(index + 1, value)
            search(index + 1, value | nums[index])

        search(0, 0)
        return count


if __name__ == "__main__":
    test_cases = [(([3, 1],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countMaxOrSubsets(*args) == expected
