#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#

import os
import sys
from collections import Counter
from heapq import heappop, heappush


# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""

        heap = [(-count, character) for character, count in counts.items()]
        from heapq import heapify

        heapify(heap)
        answer = []
        previous_count, previous_character = 0, ""
        while heap:
            count, character = heappop(heap)
            answer.append(character)
            if previous_count < 0:
                heappush(heap, (previous_count, previous_character))
            previous_count, previous_character = count + 1, character
        return "".join(answer)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.reorganizeString,
            ("aab",),
            lambda value: sorted(value) == list("aab") and value[0] != value[1],
        ),
        (solution.reorganizeString, ("aaab",), lambda value: value == ""),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert expected(result)
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 实际 = {result}")
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
