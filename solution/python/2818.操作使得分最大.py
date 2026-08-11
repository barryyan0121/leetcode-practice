#
# @lc app=leetcode.cn id=2818 lang=python3
# @lcpr version=30203
#
# [2818] 操作使得分最大
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        maximum = max(nums)
        smallest_prime = list(range(maximum + 1))
        for value in range(2, int(maximum**0.5) + 1):
            if smallest_prime[value] == value:
                for multiple in range(value * value, maximum + 1, value):
                    if smallest_prime[multiple] == multiple:
                        smallest_prime[multiple] = value

        scores = []
        for number in nums:
            score = 0
            while number > 1:
                prime = smallest_prime[number]
                score += 1
                while number % prime == 0:
                    number //= prime
            scores.append(score)

        left = [-1] * len(nums)
        stack = []
        for index, score in enumerate(scores):
            while stack and scores[stack[-1]] < score:
                stack.pop()
            left[index] = stack[-1] if stack else -1
            stack.append(index)

        right = [len(nums)] * len(nums)
        stack = []
        for index in range(len(nums) - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[index]:
                stack.pop()
            right[index] = stack[-1] if stack else len(nums)
            stack.append(index)

        answer = 1
        for index in sorted(range(len(nums)), key=nums.__getitem__, reverse=True):
            uses = min(k, (index - left[index]) * (right[index] - index))
            answer = answer * pow(nums[index], uses, mod) % mod
            k -= uses
            if not k:
                break
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumScore([8, 3, 9, 3, 8], 2) == 81
    assert solution.maximumScore([19, 12, 14, 6, 10, 18], 3) == 4788
    print("测试用例通过")
