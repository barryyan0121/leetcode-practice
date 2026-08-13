from collections import Counter
from typing import List


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        counts = Counter(word[:k] for word in words if len(word) >= k)
        return sum(count >= 2 for count in counts.values())


if __name__ == "__main__":
    assert Solution().prefixConnected(["apple", "apply", "banana", "bandit"], 2) == 2
