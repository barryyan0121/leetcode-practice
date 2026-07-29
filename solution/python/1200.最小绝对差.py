from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        difference = min(right - left for left, right in zip(arr, arr[1:]))
        return [
            [left, right]
            for left, right in zip(arr, arr[1:])
            if right - left == difference
        ]


if __name__ == "__main__":
    test_cases = [
        ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
        ([1, 3, 6, 10, 15], [[1, 3]]),
    ]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().minimumAbsDifference(arr) == expected
