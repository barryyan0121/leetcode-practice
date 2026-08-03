# @lc app=leetcode.cn id=1593 lang=python3


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        answer = 0

        def search(start: int, used: set[str]) -> None:
            nonlocal answer
            if len(used) + len(s) - start <= answer:
                return
            if start == len(s):
                answer = max(answer, len(used))
                return
            for end in range(start + 1, len(s) + 1):
                part = s[start:end]
                if part not in used:
                    used.add(part)
                    search(end, used)
                    used.remove(part)

        search(0, set())
        return answer


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxUniqueSplit, ("ababccc",), 5),
        (solution.maxUniqueSplit, ("aba",), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1593 题 "拆分字符串使得子字符串都是唯一的" 所有测试用例通过')
