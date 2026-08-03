# @lc app=leetcode.cn id=2151 lang=python3


class Solution:
    def maximumGood(self, statements: list[list[int]]) -> int:
        people = len(statements)
        answer = 0
        for mask in range(1 << people):
            valid = True
            for person in range(people):
                if not (mask >> person) & 1:
                    continue
                for other, statement in enumerate(statements[person]):
                    if statement != 2 and statement != ((mask >> other) & 1):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                answer = max(answer, mask.bit_count())
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maximumGood, ([[2, 1], [1, 2]],), 2),
        (solution.maximumGood, ([[2, 0], [0, 2]],), 1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 2151 题 "基于陈述统计最多好人数" 所有测试用例通过')
