"""2610. 转换二维数组"""


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        rows = []
        counts = {}
        for value in nums:
            row = counts.get(value, 0)
            if row == len(rows):
                rows.append([])
            rows[row].append(value)
            counts[value] = row + 1
        return rows


if __name__ == "__main__":
    test_cases = [(([1, 3, 4, 1, 2, 3, 1],), [[1, 3, 4, 2], [1, 3], [1]])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findMatrix(*args) == expected
