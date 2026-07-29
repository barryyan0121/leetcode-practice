from bisect import bisect_right
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        states = {float("-inf"): 0}
        for value in arr1:
            next_states = {}
            for previous, changes in states.items():
                if value > previous:
                    next_states[value] = min(
                        next_states.get(value, float("inf")), changes
                    )
                index = bisect_right(arr2, previous)
                if index < len(arr2):
                    replacement = arr2[index]
                    next_states[replacement] = min(
                        next_states.get(replacement, float("inf")), changes + 1
                    )
            states = next_states
            if not states:
                return -1
        return min(states.values())


if __name__ == "__main__":
    test_cases = [([1, 5, 3, 6, 7], [1, 3, 2, 4], 1), ([1, 5, 3, 6, 7], [4, 3, 1], 2)]
    for _, (arr1, arr2, expected) in enumerate(test_cases):
        assert Solution().makeArrayIncreasing(arr1, arr2) == expected
