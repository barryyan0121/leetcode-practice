#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#

import os
import sys
from collections import defaultdict
from typing import *


# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        owner = {}
        for name, first, *emails in accounts:
            owner[first] = name
            for email in emails:
                owner[email] = name
                graph[first].add(email)
                graph[email].add(first)

        answer = []
        visited = set()
        for email in owner:
            if email in visited:
                continue
            stack = [email]
            visited.add(email)
            component = []
            while stack:
                current = stack.pop()
                component.append(current)
                for neighbor in graph[current] - visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
            answer.append([owner[email], *sorted(component)])
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["Mary", "mary@mail.com"],
    ]
    test_cases = [(solution.accountsMerge, (accounts,), expected)]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = sorted(func(*args))
        try:
            assert result == sorted(expected)
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
