#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        targets = deque(sorted(range(len(nums2)), key=nums2.__getitem__))
        answer = [0] * len(nums1)
        for number in sorted(nums1):
            index = targets.popleft() if number > nums2[targets[0]] else targets.pop()
            answer[index] = number
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.advantageCount, ([2, 7, 11, 15], [1, 10, 4, 11]), [2, 11, 7, 15]),
        (solution.advantageCount, ([12, 24, 8, 32], [13, 25, 32, 11]), [24, 32, 8, 12]),
        (solution.advantageCount, ([1], [2]), [1]),
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
