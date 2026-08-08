from typing import List


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        slots1.sort()
        slots2.sort()
        first = second = 0
        while first < len(slots1) and second < len(slots2):
            start = max(slots1[first][0], slots2[second][0])
            end = min(slots1[first][1], slots2[second][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[first][1] < slots2[second][1]:
                first += 1
            else:
                second += 1
        return []


if __name__ == "__main__":
    test_cases = [
        (
            [[10, 50], [60, 120], [140, 210]],
            [[0, 15], [60, 70]],
            8,
            [60, 68],
        )
    ]
    for _, (slots1, slots2, duration, expected) in enumerate(test_cases):
        assert Solution().minAvailableDuration(slots1, slots2, duration) == expected
