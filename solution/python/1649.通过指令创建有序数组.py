# @lc app=leetcode.cn id=1649 lang=python3


class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        mod = 10**9 + 7
        size = max(instructions) + 2
        tree = [0] * size

        def query(index: int) -> int:
            total = 0
            while index:
                total += tree[index]
                index -= index & -index
            return total

        def update(index: int) -> None:
            while index < size:
                tree[index] += 1
                index += index & -index

        answer = 0
        seen = 0
        for value in instructions:
            less = query(value - 1)
            greater = seen - query(value)
            answer = (answer + min(less, greater)) % mod
            update(value)
            seen += 1
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.createSortedArray, ([1, 5, 6, 2],), 1),
        (solution.createSortedArray, ([1, 2, 3, 6, 5, 4],), 3),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1649 题 "通过指令创建有序数组" 所有测试用例通过')
