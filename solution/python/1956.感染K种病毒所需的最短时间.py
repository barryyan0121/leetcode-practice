"""1956. 感染 K 种病毒所需的最短时间"""


class Solution:
    def minDayskVariants(self, points: list[list[int]], k: int) -> int:
        def enough(days: int) -> bool:
            rectangles = []
            for x, y in points:
                rectangles.append(
                    (x + y - days, x + y + days, x - y - days, x - y + days)
                )
            candidates_x = {left for left, _, _, _ in rectangles}
            candidates_x |= {left + 1 for left, _, _, _ in rectangles}
            for current_x in candidates_x:
                active = [
                    item for item in rectangles if item[0] <= current_x <= item[1]
                ]
                candidates_y = {item[2] for item in active}
                candidates_y |= {item[2] + 1 for item in active}
                for current_y in candidates_y:
                    if (current_x - current_y) % 2:
                        continue
                    if (
                        sum(left <= current_y <= right for _, _, left, right in active)
                        >= k
                    ):
                        return True
            return False

        low, high = 0, 2 * 10**9
        while low < high:
            middle = (low + high) // 2
            if enough(middle):
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [
        (([[1, 1], [6, 1]], 2), 3),
        (([[3, 3], [1, 2], [9, 2]], 2), 2),
        (([[3, 3], [1, 2], [9, 2]], 3), 4),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minDayskVariants(*args) == expected
