#
# @lc app=leetcode.cn id=1865 lang=python3
# @lcpr version=30201
#
# [1865] 找出和为指定值的下标对
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from collections import Counter


# @lc code=start
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.cnt[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.cnt[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.nums1:
            ans += self.cnt[tot - num]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end

if __name__ == "__main__":
    nums1 = [1, 1, 2, 2, 2, 3]
    nums2 = [1, 4, 5, 2, 5, 4]
    obj = FindSumPairs(nums1, nums2)
    test_cases = [
        # 存储函数和参数，而不是执行结果
        (obj.count, (7,), 8),
        (obj.add, (3, 2), None),
        # 使用lambda延迟获取nums2的值
        (lambda: obj.nums2, (), [1, 4, 5, 4, 5, 4]),
        (obj.count, (8,), 2),
        (obj.count, (4,), 1),
        (obj.add, (0, 1), None),
        (lambda: obj.nums2, (), [2, 4, 5, 4, 5, 4]),
        (obj.add, (1, 1), None),
        (lambda: obj.nums2, (), [2, 5, 5, 4, 5, 4]),
        (obj.count, (7,), 11),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n={args}, result={result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n={args}, 期望={expected}, 实际={result}")

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]\n[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]\n
# @lcpr case=end

#
