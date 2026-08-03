# @lc app=leetcode.cn id=1477 lang=python3


class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        infinity = 10**9
        best = [infinity] * (len(arr) + 1)
        first_index = {0: 0}
        prefix = 0
        answer = infinity
        for end, value in enumerate(arr, 1):
            prefix += value
            best[end] = best[end - 1]
            if prefix - target in first_index:
                start = first_index[prefix - target]
                length = end - start
                answer = min(answer, length + best[start])
                best[end] = min(best[end], length)
            first_index.setdefault(prefix, end)
        return -1 if answer >= infinity else answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.minSumOfLengths, ([3, 2, 2, 4, 3], 3), 2)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1477 题 "找两个和为目标值且不重叠的子数组" 所有测试用例通过')
