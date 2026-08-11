class Solution:
    def buttonWithLongestTime(self, events: list[list[int]]) -> int:
        answer, longest, previous = events[0][0], events[0][1], events[0][1]
        for index, timestamp in events[1:]:
            duration = timestamp - previous
            if duration > longest or (duration == longest and index < answer):
                answer, longest = index, duration
            previous = timestamp
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[1, 2], [2, 5], [3, 9], [1, 15]],), 1),
        (([[10, 5], [1, 7]],), 10),
    ]
    for _, ((events,), expected) in enumerate(test_cases):
        assert Solution().buttonWithLongestTime(events) == expected
