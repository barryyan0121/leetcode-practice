# @lc app=leetcode.cn id=1712 lang=python3


class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        from bisect import bisect_left, bisect_right

        mod = 10**9 + 7
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        answer = 0
        for left_end in range(1, len(nums) - 1):
            first = prefix[left_end]
            lower = bisect_left(prefix, 2 * first, left_end + 1, len(nums))
            upper = bisect_right(prefix, (prefix[-1] + first) // 2, lower, len(nums))
            answer += max(0, upper - lower)
        return answer % mod


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.waysToSplit, ([1, 2, 2, 2, 5, 0],), 3),
        (solution.waysToSplit, ([3, 2, 1],), 0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1712 题 "将数组分成三个子数组的方案数" 所有测试用例通过')
