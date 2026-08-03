# @lc app=leetcode.cn id=1461 lang=python3


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[index : index + k] for index in range(len(s) - k + 1)}) == 1 << k


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.hasAllCodes, ("00110110", 2), True),
        (solution.hasAllCodes, ("0110", 2), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print(
        '第 1461 题 "检查一个字符串是否包含所有长度为 K 的二进制子串" 所有测试用例通过'
    )
