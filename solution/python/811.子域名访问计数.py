#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = Counter()
        for item in cpdomains:
            count, domain = item.split()
            parts = domain.split(".")
            for index in range(len(parts)):
                visits[".".join(parts[index:])] += int(count)
        return [f"{count} {domain}" for domain, count in visits.items()]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.subdomainVisits,
            (["9001 discuss.leetcode.com"],),
            {"9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"},
        ),
        (
            solution.subdomainVisits,
            (
                [
                    "900 google.mail.com",
                    "50 yahoo.com",
                    "1 intel.mail.com",
                    "5 wiki.org",
                ],
            ),
            {
                "900 google.mail.com",
                "901 mail.com",
                "951 com",
                "50 yahoo.com",
                "1 intel.mail.com",
                "5 wiki.org",
                "5 org",
            },
        ),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert set(result) == expected
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
