class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        i = len(arr) - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i >= 0:
            j = len(arr) - 1
            while arr[j] >= arr[i]:
                j -= 1
            while j > i + 1 and arr[j] == arr[j - 1]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        return arr


if __name__ == "__main__":
    test_cases = [([3, 2, 1], [3, 1, 2]), ([3, 1, 1, 3], [1, 3, 1, 3])]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().prevPermOpt1(arr) == expected
