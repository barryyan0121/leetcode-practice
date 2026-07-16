#
# @lc app=leetcode.cn id=943 lang=python3
#
# [943] 最短超级串
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        words = list(dict.fromkeys(words))
        words = [
            word
            for word in words
            if not any(word != other and word in other for other in words)
        ]
        n = len(words)
        overlap = [[0] * n for _ in range(n)]
        for first in range(n):
            for second in range(n):
                if first == second:
                    continue
                for length in range(min(len(words[first]), len(words[second])), 0, -1):
                    if words[first].endswith(words[second][:length]):
                        overlap[first][second] = length
                        break

        dp = [[-1] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        for index in range(n):
            dp[1 << index][index] = 0
        for mask in range(1 << n):
            for last in range(n):
                if dp[mask][last] < 0:
                    continue
                for following in range(n):
                    if mask >> following & 1:
                        continue
                    next_mask = mask | 1 << following
                    candidate = dp[mask][last] + overlap[last][following]
                    if candidate > dp[next_mask][following]:
                        dp[next_mask][following] = candidate
                        parent[next_mask][following] = last

        mask = (1 << n) - 1
        last = max(range(n), key=lambda index: dp[mask][index])
        order = []
        while last != -1:
            order.append(last)
            previous = parent[mask][last]
            mask ^= 1 << last
            last = previous
        order.reverse()
        answer = words[order[0]]
        for first, second in zip(order, order[1:]):
            answer += words[second][overlap[first][second] :]
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.shortestSuperstring, (["alex", "loves", "leetcode"],), 17),
        (
            solution.shortestSuperstring,
            (["catg", "ctaagt", "gcta", "ttca", "atgcatc"],),
            16,
        ),
        (solution.shortestSuperstring, (["abc", "bc", "c"],), 3),
    ]
    all_passed = True
    for idx, (func, args, expected_length) in enumerate(test_cases):
        result = func(*args)
        expected = len(result) == expected_length and all(
            word in result for word in args[0]
        )
        try:
            assert expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望长度 = {expected_length}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
