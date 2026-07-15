#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        sequence = []

        def search(index: int) -> bool:
            if index == len(num):
                return len(sequence) >= 3
            value = 0
            for end in range(index, len(num)):
                if end > index and num[index] == "0":
                    break
                value = value * 10 + int(num[end])
                if value > 2**31 - 1:
                    break
                if len(sequence) >= 2:
                    expected = sequence[-1] + sequence[-2]
                    if value < expected:
                        continue
                    if value > expected:
                        break
                sequence.append(value)
                if search(end + 1):
                    return True
                sequence.pop()
            return False

        return sequence if search(0) else []


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.splitIntoFibonacci, ("1101111",), [11, 0, 11, 11]),
        (solution.splitIntoFibonacci, ("112358130",), []),
        (solution.splitIntoFibonacci, ("0123",), []),
        (solution.splitIntoFibonacci, ("123456579",), [123, 456, 579]),
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
