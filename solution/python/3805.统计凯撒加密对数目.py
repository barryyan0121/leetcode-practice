from collections import Counter
from typing import List


class Solution:
    def countPairs(self, words: List[str]) -> int:
        groups = Counter()
        for word in words:
            first = ord(word[0]) - ord("a")
            key = tuple((ord(char) - ord("a") - first) % 26 for char in word)
            groups[key] += 1
        return sum(count * (count - 1) // 2 for count in groups.values())


if __name__ == "__main__":
    s = Solution()
    assert s.countPairs(["fusion", "layout"]) == 1
    assert s.countPairs(["ab", "aa", "za", "aa"]) == 2
