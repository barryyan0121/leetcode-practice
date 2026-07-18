class Solution:
    def findInMountainArray(self, target: int, mountain_arr) -> int:
        left, right = 0, mountain_arr.length() - 1
        while left < right:
            middle = (left + right) // 2
            if mountain_arr.get(middle) < mountain_arr.get(middle + 1):
                left = middle + 1
            else:
                right = middle
        peak = left

        left, right = 0, peak
        while left <= right:
            middle = (left + right) // 2
            value = mountain_arr.get(middle)
            if value == target:
                return middle
            if value < target:
                left = middle + 1
            else:
                right = middle - 1

        left, right = peak + 1, mountain_arr.length() - 1
        while left <= right:
            middle = (left + right) // 2
            value = mountain_arr.get(middle)
            if value == target:
                return middle
            if value > target:
                left = middle + 1
            else:
                right = middle - 1
        return -1


if __name__ == "__main__":

    class MountainArray:
        def __init__(self, values: list[int]) -> None:
            self.values = values

        def get(self, index: int) -> int:
            return self.values[index]

        def length(self) -> int:
            return len(self.values)

    test_cases = [
        ([1, 2, 3, 4, 5, 3, 1], 3, 2),
        ([0, 1, 2, 4, 2, 1], 3, -1),
        ([1, 5, 2], 2, 2),
        ([1, 3, 5, 7, 6, 4, 2], 7, 3),
    ]
    for _, (values, target, expected) in enumerate(test_cases):
        assert Solution().findInMountainArray(target, MountainArray(values)) == expected
