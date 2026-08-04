class Solution:
    def maxScore(self, points: list[int], m: int) -> int:
        draxemilon = (points, m)
        size = len(points)

        def feasible(score: int) -> bool:
            moves = 1
            visits = 1
            for index in range(size - 2):
                required = (score + points[index] - 1) // points[index]
                extra = 0
                if visits < required:
                    extra = required - visits
                    moves += 2 * extra
                moves += 1
                visits = extra + 1
                if moves > m:
                    return False
            required = (score + points[-2] - 1) // points[-2]
            minimum_bounces = max(0, required - visits)
            last_required = (score + points[-1] - 1) // points[-1]
            stop_here = 2 * max(minimum_bounces, last_required)
            move_to_last = 2 * max(minimum_bounces, last_required - 1) + 1
            return moves + min(stop_here, move_to_last) <= m

        low, high = 0, min(points) * m + 1
        while low + 1 < high:
            middle = (low + high) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle
        return low


if __name__ == "__main__":
    test_cases = [
        (([2, 4], 3), 4),
        (([1, 2, 3], 5), 2),
        (([1, 1, 1, 1, 1], 5), 1),
    ]
    for _, ((points, m), expected) in enumerate(test_cases):
        assert Solution().maxScore(points, m) == expected
