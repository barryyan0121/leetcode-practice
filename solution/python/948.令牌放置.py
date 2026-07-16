#
# @lc app=leetcode.cn id=948 lang=python3
#
# [948] 令牌放置
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = answer = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                answer = max(answer, score)
            elif score:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.bagOfTokensScore, ([100], 50), 0),
        (solution.bagOfTokensScore, ([100, 200], 150), 1),
        (solution.bagOfTokensScore, ([100, 200, 300, 400], 200), 2),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
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
