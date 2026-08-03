# @lc app=leetcode.cn id=1409 lang=python3


class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        permutation = list(range(1, m + 1))
        result = []
        for query in queries:
            index = permutation.index(query)
            result.append(index)
            permutation.pop(index)
            permutation.insert(0, query)
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.processQueries, ([3, 1, 2, 1], 5), [2, 1, 2, 1])]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1409 题 "查询带键的排列" 所有测试用例通过')
