class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        last = len(arr) - 1
        duplicate_count = 0
        index = 0
        while index <= last - duplicate_count:
            if arr[index] == 0:
                if index == last - duplicate_count:
                    arr[last] = 0
                    last -= 1
                    break
                duplicate_count += 1
            index += 1
        for index in range(last - duplicate_count, -1, -1):
            if arr[index] == 0:
                arr[index + duplicate_count] = 0
                duplicate_count -= 1
                arr[index + duplicate_count] = 0
            else:
                arr[index + duplicate_count] = arr[index]


if __name__ == "__main__":
    test_cases = [
        ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 1, 2, 3], [0, 0, 1, 2]),
        ([1, 2, 3, 0], [1, 2, 3, 0]),
        ([0, 0, 0], [0, 0, 0]),
    ]
    for _, (arr, expected) in enumerate(test_cases):
        Solution().duplicateZeros(arr)
        assert arr == expected
