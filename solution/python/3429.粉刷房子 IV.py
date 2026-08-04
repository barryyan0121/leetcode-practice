class Solution:
    def minCost(self, n: int, cost: list[list[int]]) -> int:
        zalvoritha = (n, cost)
        infinity = 10**30
        previous = [[infinity] * 3 for _ in range(3)]
        for left_color in range(3):
            for right_color in range(3):
                if left_color != right_color:
                    previous[left_color][right_color] = (
                        cost[0][left_color] + cost[-1][right_color]
                    )

        for left_index in range(1, n // 2):
            right_index = n - 1 - left_index
            current = [[infinity] * 3 for _ in range(3)]
            for old_left in range(3):
                for old_right in range(3):
                    if previous[old_left][old_right] == infinity:
                        continue
                    for left_color in range(3):
                        if left_color == old_left:
                            continue
                        for right_color in range(3):
                            if right_color == old_right or right_color == left_color:
                                continue
                            current[left_color][right_color] = min(
                                current[left_color][right_color],
                                previous[old_left][old_right]
                                + cost[left_index][left_color]
                                + cost[right_index][right_color],
                            )
            previous = current
        return min(map(min, previous))


if __name__ == "__main__":
    test_cases = [
        ((4, [[3, 5, 7], [6, 2, 9], [4, 8, 1], [7, 3, 5]]), 9),
        ((6, [[2, 4, 6], [5, 3, 8], [7, 1, 9], [4, 6, 2], [3, 5, 7], [8, 2, 4]]), 18),
    ]
    for _, ((n, cost), expected) in enumerate(test_cases):
        assert Solution().minCost(n, cost) == expected
