class Solution:
    def minHeightShelves(self, books: list[list[int]], shelf_width: int) -> int:
        dp = [0] + [float("inf")] * len(books)
        for index in range(1, len(books) + 1):
            width = height = 0
            for start in range(index, 0, -1):
                width += books[start - 1][0]
                if width > shelf_width:
                    break
                height = max(height, books[start - 1][1])
                dp[index] = min(dp[index], dp[start - 1] + height)
        return dp[-1]


if __name__ == "__main__":
    test_cases = [
        ([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4, 6),
        ([[1, 3], [2, 4], [3, 2]], 6, 4),
        ([[7, 3]], 7, 3),
        ([[2, 1], [2, 10], [2, 1]], 4, 11),
    ]
    for _, (books, shelf_width, expected) in enumerate(test_cases):
        assert Solution().minHeightShelves(books, shelf_width) == expected
