"""2268. 最少按键次数"""

from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counts = sorted(Counter(s).values(), reverse=True)
        return sum((i // 9 + 1) * count for i, count in enumerate(counts))

if __name__ == "__main__":
    assert Solution().minimumKeypresses("apple") == 5
