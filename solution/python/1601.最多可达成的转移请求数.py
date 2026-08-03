# @lc app=leetcode.cn id=1601 lang=python3


class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        answer = 0
        for mask in range(1 << len(requests)):
            if mask.bit_count() <= answer:
                continue
            balance = [0] * n
            for index, (start, end) in enumerate(requests):
                if mask >> index & 1:
                    balance[start] -= 1
                    balance[end] += 1
            if all(value == 0 for value in balance):
                answer = mask.bit_count()
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.maximumRequests,
            (5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]),
            5,
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1601 题 "最多可达成的转移请求数" 所有测试用例通过')
