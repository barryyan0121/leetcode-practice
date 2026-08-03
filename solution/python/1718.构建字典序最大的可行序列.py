# @lc app=leetcode.cn id=1718 lang=python3


class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        sequence = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def search(index: int) -> bool:
            while index < len(sequence) and sequence[index]:
                index += 1
            if index == len(sequence):
                return True
            for value in range(n, 0, -1):
                if used[value] or (
                    value > 1
                    and (index + value >= len(sequence) or sequence[index + value])
                ):
                    continue
                sequence[index] = value
                if value > 1:
                    sequence[index + value] = value
                used[value] = True
                if search(index + 1):
                    return True
                used[value] = False
                sequence[index] = 0
                if value > 1:
                    sequence[index + value] = 0
            return False

        search(0)
        return sequence


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.constructDistancedSequence, (3,), [3, 1, 2, 3, 2]),
        (solution.constructDistancedSequence, (2,), [2, 1, 2]),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1718 题 "构建字典序最大的可行序列" 所有测试用例通过')
