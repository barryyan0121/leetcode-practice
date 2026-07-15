#
# @lc app=leetcode.cn id=854 lang=python3
#
# [854] 相似度为 K 的字符串
#

import os
import sys


# @lc code=start
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        queue = [s1]
        visited = {s1}
        swaps = 0
        while queue:
            next_queue = []
            for current in queue:
                if current == s2:
                    return swaps
                index = next(i for i in range(len(s1)) if current[i] != s2[i])
                for other in range(index + 1, len(s1)):
                    if current[other] == s2[index] and current[other] != s2[other]:
                        characters = list(current)
                        characters[index], characters[other] = (
                            characters[other],
                            characters[index],
                        )
                        candidate = "".join(characters)
                        if candidate not in visited:
                            visited.add(candidate)
                            next_queue.append(candidate)
            queue = next_queue
            swaps += 1
        return swaps


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.kSimilarity, ("ab", "ba"), 1),
        (solution.kSimilarity, ("abc", "bca"), 2),
        (solution.kSimilarity, ("aabc", "abca"), 2),
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
