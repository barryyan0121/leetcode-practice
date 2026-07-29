from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        kept = arr[0]
        deleted = float("-inf")
        answer = arr[0]
        for value in arr[1:]:
            deleted = max(deleted + value, kept)
            kept = max(kept + value, value)
            answer = max(answer, kept, deleted)
        return answer


if __name__ == "__main__":
    test_cases = [([1, -2, 0, 3], 4), ([1, -2, -2, 3], 3), ([-1, -1, -1], -1)]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().maximumSum(arr) == expected
