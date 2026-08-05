"""2044. 统计按位或能得到最大值的子集数目"""


class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        target = 0
        for value in nums:
            target |= value
        answer = 0

        def dfs(index: int, current: int) -> None:
            nonlocal answer
            if index == len(nums):
                answer += current == target
                return
            dfs(index + 1, current | nums[index])
            dfs(index + 1, current)

        dfs(0, 0)
        return answer


if __name__ == "__main__":
    test_cases = [(([3, 1],), 2), (([2, 2, 2],), 7)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countMaxOrSubsets(*args) == expected
