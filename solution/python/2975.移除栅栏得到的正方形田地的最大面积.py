class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: list[int], vFences: list[int]
    ) -> int:
        horizontal = [1, m] + hFences
        vertical = [1, n] + vFences
        heights = {
            first - second
            for first in horizontal
            for second in horizontal
            if first > second
        }
        side = max(
            (
                first - second
                for first in vertical
                for second in vertical
                if first > second and first - second in heights
            ),
            default=0,
        )
        return side * side % (10**9 + 7) if side else -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximizeSquareArea(4, 3, [2, 3], [2]) == 4
    assert solution.maximizeSquareArea(6, 7, [2], [4]) == -1
