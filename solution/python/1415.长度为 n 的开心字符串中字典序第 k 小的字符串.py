# @lc app=leetcode.cn id=1415 lang=python3


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        letters = "abc"
        for position in range(n):
            for letter in letters:
                if result and result[-1] == letter:
                    continue
                block = 1 << (n - position - 1)
                if k > block:
                    k -= block
                else:
                    result.append(letter)
                    break
            else:
                return ""
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.getHappyString, (1, 3), "c"),
        (solution.getHappyString, (3, 9), "cab"),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1415 题 "长度为 n 的开心字符串中字典序第 k 小的字符串" 所有测试用例通过')
