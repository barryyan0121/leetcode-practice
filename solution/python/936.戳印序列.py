#
# @lc app=leetcode.cn id=936 lang=python3
#
# [936] 戳印序列
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        characters = list(target)
        used = set()
        answer = []
        erased = 0
        while erased < len(target):
            progress = False
            for start in range(len(target) - len(stamp) + 1):
                if start in used:
                    continue
                window = characters[start : start + len(stamp)]
                if all(
                    current == "?" or current == expected
                    for current, expected in zip(window, stamp)
                ) and any(current != "?" for current in window):
                    for index in range(start, start + len(stamp)):
                        if characters[index] != "?":
                            characters[index] = "?"
                            erased += 1
                    used.add(start)
                    answer.append(start)
                    progress = True
            if not progress:
                return []
        return answer[::-1]


# @lc code=end


def valid(stamp, target, moves):
    result = ["?"] * len(target)
    for start in moves:
        result[start : start + len(stamp)] = stamp
    return "".join(result) == target and len(moves) <= 10 * len(target)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.movesToStamp, ("abc", "ababc"), valid),
        (solution.movesToStamp, ("abca", "aabcaca"), valid),
        (
            solution.movesToStamp,
            ("aye", "eyeye"),
            lambda stamp, target, moves: moves == [],
        ),
    ]
    all_passed = True
    for idx, (func, args, checker) in enumerate(test_cases):
        result = func(*args)
        expected = checker(*args, result)
        try:
            assert expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 实际 = {result}")
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
