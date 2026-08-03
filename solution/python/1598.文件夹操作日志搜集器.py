# @lc app=leetcode.cn id=1598 lang=python3


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                depth = max(0, depth - 1)
            elif log != "./":
                depth += 1
        return depth


if __name__ == "__main__":
    solution = Solution()
    test_cases = [(solution.minOperations, (["d1/", "d2/", "../", "d21/", "./"],), 2)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1598 题 "文件夹操作日志搜集器" 所有测试用例通过')
