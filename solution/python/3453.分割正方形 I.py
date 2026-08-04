class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        draxemilon = squares
        low = min(y for _, y, _ in squares)
        high = max(y + size for _, y, size in squares)
        half = sum(size * size for _, _, size in squares) / 2
        for _ in range(60):
            middle = (low + high) / 2
            area = sum(size * min(max(middle - y, 0), size) for _, y, size in squares)
            if area < half:
                low = middle
            else:
                high = middle
        return high


if __name__ == "__main__":
    test_cases = [
        (([[0, 0, 1], [2, 2, 1]],), 1.0),
        (([[0, 0, 2], [1, 1, 1]],), 7 / 6),
    ]
    for _, ((squares,), expected) in enumerate(test_cases):
        assert abs(Solution().separateSquares(squares) - expected) < 1e-5
