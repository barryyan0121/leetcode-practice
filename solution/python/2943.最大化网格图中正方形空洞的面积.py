"""2943. 最大化网格图中正方形空洞的面积"""


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: list[int], vBars: list[int]
    ) -> int:
        def longest(bars: list[int]) -> int:
            bars.sort()
            best = current = 1
            for left, right in zip(bars, bars[1:]):
                current = current + 1 if right == left + 1 else 1
                best = max(best, current)
            return best + 1

        side = min(longest(hBars), longest(vBars))
        return side * side


if __name__ == "__main__":
    assert Solution().maximizeSquareHoleArea(2, 3, [2, 3], [2, 3]) == 9
