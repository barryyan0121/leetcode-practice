from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = [0]
        for word in arr:
            mask = 0
            for char in word:
                bit = 1 << (ord(char) - ord("a"))
                if mask & bit:
                    break
                mask |= bit
            else:
                masks += [mask | old for old in masks if not mask & old]
        return max(mask.bit_count() for mask in masks)


if __name__ == "__main__":
    test_cases = [(["un", "iq", "ue"], 4), (["cha", "r", "act", "ers"], 6)]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().maxLength(arr) == expected
