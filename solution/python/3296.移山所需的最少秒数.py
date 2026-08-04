from math import isqrt


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        def can_finish(seconds: int) -> bool:
            removed = 0
            for time in workerTimes:
                units = (isqrt(1 + 8 * (seconds // time)) - 1) // 2
                removed += units
                if removed >= mountainHeight:
                    return True
            return False

        low, high = 0, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while low < high:
            middle = (low + high) // 2
            if can_finish(middle):
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [
        ((4, [2, 1, 1]), 3),
        ((10, [3, 2, 2, 4]), 12),
        ((5, [1]), 15),
    ]
    for _, ((mountain_height, worker_times), expected) in enumerate(test_cases):
        assert Solution().minNumberOfSeconds(mountain_height, worker_times) == expected
