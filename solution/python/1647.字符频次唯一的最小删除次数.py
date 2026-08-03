# @lc app=leetcode.cn id=1647 lang=python3


class Solution:
    def minDeletions(self, s: str) -> int:
        counts = sorted((s.count(char) for char in set(s)), reverse=True)
        used = set()
        answer = 0
        for count in counts:
            while count and count in used:
                count -= 1
                answer += 1
            used.add(count)
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minDeletions, ("aab",), 0),
        (solution.minDeletions, ("aaabbbcc",), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1647 题 "字符频次唯一的最小删除次数" 所有测试用例通过')
