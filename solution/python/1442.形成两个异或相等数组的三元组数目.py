# @lc app=leetcode.cn id=1442 lang=python3


class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        result = prefix = 0
        count = {0: 1}
        total_index = {0: 0}
        for index, value in enumerate(arr):
            prefix ^= value
            result += count.get(prefix, 0) * index - total_index.get(prefix, 0)
            count[prefix] = count.get(prefix, 0) + 1
            total_index[prefix] = total_index.get(prefix, 0) + index + 1
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.countTriplets, ([2, 3, 1, 6, 7],), 4)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1442 题 "形成两个异或相等数组的三元组数目" 所有测试用例通过')
