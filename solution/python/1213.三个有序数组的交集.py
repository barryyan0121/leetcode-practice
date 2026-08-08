from typing import List


class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        return sorted(set(arr1) & set(arr2) & set(arr3))


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8], [1, 5])]
    for _, (arr1, arr2, arr3, expected) in enumerate(test_cases):
        assert Solution().arraysIntersection(arr1, arr2, arr3) == expected
