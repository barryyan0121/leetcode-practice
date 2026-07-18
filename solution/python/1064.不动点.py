class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] < middle:
                left = middle + 1
            else:
                right = middle - 1
        return left if left < len(arr) and arr[left] == left else -1


if __name__ == "__main__":
    test_cases = [
        ([-10, -5, 0, 3, 7], 3),
        ([0, 2, 5, 8, 17], 0),
        ([-10, -5, 3, 4, 7, 9], -1),
    ]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().fixedPoint(arr) == expected
