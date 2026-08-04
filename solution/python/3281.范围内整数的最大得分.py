class Solution:
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        start.sort()

        def feasible(gap: int) -> bool:
            previous = start[0]
            for left in start[1:]:
                previous = max(left, previous + gap)
                if previous > left + d:
                    return False
            return True

        low, high = 0, start[-1] + d - start[0] + 1
        while low + 1 < high:
            middle = (low + high) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle
        return low


if __name__ == "__main__":
    test_cases = [(([6, 0, 3], 2), 4), (([2, 6, 13, 13], 5), 5)]
    for _, ((start, d), expected) in enumerate(test_cases):
        assert Solution().maxPossibleScore(start, d) == expected
