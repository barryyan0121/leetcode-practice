# @lc app=leetcode.cn id=1505 lang=python3


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        positions = [[] for _ in range(10)]
        for index, digit in enumerate(num):
            positions[int(digit)].append(index)
        pointers = [0] * 10
        size = len(num)
        bit = [0] * (size + 1)

        def add(index: int, value: int) -> None:
            index += 1
            while index <= size:
                bit[index] += value
                index += index & -index

        def prefix(index: int) -> int:
            total = 0
            while index:
                total += bit[index]
                index -= index & -index
            return total

        for index in range(size):
            add(index, 1)
        result = []
        for output_index in range(size):
            for digit in range(10):
                if pointers[digit] >= len(positions[digit]):
                    continue
                original = positions[digit][pointers[digit]]
                moves = prefix(original)
                if moves <= k:
                    k -= moves
                    pointers[digit] += 1
                    add(original, -1)
                    result.append(str(digit))
                    break
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minInteger, ("4321", 4), "1342"),
        (solution.minInteger, ("100", 1), "010"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1505 题 "最多 K 次交换相邻数位后得到的最小整数" 所有测试用例通过')
