class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        rank = {value: index for index, value in enumerate(arr2)}
        return sorted(arr1, key=lambda value: (rank.get(value, len(rank)), value))


if __name__ == "__main__":
    test_cases = [
        (
            [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
            [2, 1, 4, 3, 9, 6],
            [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
        ),
        ([28, 6, 22, 8, 44, 17], [22, 28, 8, 6], [22, 28, 8, 6, 17, 44]),
    ]
    for _, (arr1, arr2, expected) in enumerate(test_cases):
        assert Solution().relativeSortArray(arr1, arr2) == expected
