# @lc app=leetcode.cn id=1717 lang=python3


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(text: str, first: str, second: str, score: int) -> tuple[str, int]:
            stack, earned = [], 0
            for char in text:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    earned += score
                else:
                    stack.append(char)
            return "".join(stack), earned

        if x < y:
            s, x, y = s, y, x
            first, second = "b", "a"
        else:
            first, second = "a", "b"
        remaining, answer = remove(s, first, second, x)
        _, extra = remove(remaining, second, first, y)
        return answer + extra


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maximumGain, ("cdbcbbaaabab", 4, 5), 19),
        (solution.maximumGain, ("aabbaaxybbaabb", 5, 4), 20),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1717 题 "删除子字符串的最大得分" 所有测试用例通过')
