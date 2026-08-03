# @lc app=leetcode.cn id=1643 lang=python3


class Solution:
    def kthSmallestPath(self, destination: list[int], k: int) -> str:
        from math import comb

        vertical, horizontal = destination
        answer = []
        while vertical or horizontal:
            if horizontal:
                count = comb(vertical + horizontal - 1, horizontal - 1)
                if k <= count:
                    answer.append("H")
                    horizontal -= 1
                    continue
                k -= count
            answer.append("V")
            vertical -= 1
        return "".join(answer)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.kthSmallestPath, ([2, 3], 1), "HHHVV"),
        (solution.kthSmallestPath, ([2, 3], 3), "HHVVH"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1643 题 "第 K 条最小指令" 所有测试用例通过')
