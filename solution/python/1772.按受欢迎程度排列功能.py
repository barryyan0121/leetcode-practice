from collections import Counter
from typing import List


class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        counts = Counter()
        for response in responses:
            counts.update(set(response.split()))
        return sorted(features, key=lambda feature: -counts[feature])


if __name__ == "__main__":
    solution = Solution()
    assert solution.sortFeatures(
        ["cooler", "lock", "touch"], ["i like cooler", "lock touch", "cooler lock"]
    ) == ["cooler", "lock", "touch"]
    print("1772 passed")
