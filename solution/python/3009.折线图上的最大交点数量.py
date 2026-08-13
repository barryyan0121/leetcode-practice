class Solution:
    def maxIntersectionCount(self, y: list[int]) -> int:
        events = {}
        for first, second in zip(y, y[1:]):
            low, high = sorted((first, second))
            events[low] = events.get(low, 0) + 1
            events[high] = events.get(high, 0) - 1
        active = answer = 0
        for value in sorted(events):
            answer = max(answer, active + events[value])
            active += events[value]
        return answer


if __name__ == "__main__":
    assert Solution().maxIntersectionCount([1, 2, 1, 2, 1, 3, 2]) == 5
    assert Solution().maxIntersectionCount([2, 1, 3, 4, 5]) == 2
