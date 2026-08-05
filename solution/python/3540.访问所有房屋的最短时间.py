class Solution:
    def minTotalTime(
        self, forward: list[int], backward: list[int], queries: list[int]
    ) -> int:
        n = len(forward)
        forward_prefix = [0]
        for value in forward:
            forward_prefix.append(forward_prefix[-1] + value)
        backward_prefix = [0]
        for value in backward:
            backward_prefix.append(backward_prefix[-1] + value)
        total_forward = forward_prefix[-1]
        total_backward = backward_prefix[-1]

        def clockwise(start: int, end: int) -> int:
            if start <= end:
                return forward_prefix[end] - forward_prefix[start]
            return total_forward - forward_prefix[start] + forward_prefix[end]

        def counterclockwise(start: int, end: int) -> int:
            if start == end:
                return 0
            if start > end:
                return backward_prefix[start + 1] - backward_prefix[end + 1]
            return (
                backward_prefix[start + 1] + total_backward - backward_prefix[end + 1]
            )

        answer = 0
        current = 0
        for destination in queries:
            answer += min(
                clockwise(current, destination), counterclockwise(current, destination)
            )
            current = destination
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 4, 4], [4, 1, 2], [1, 2, 0, 2]), 12),
        (([1, 1, 1, 1], [2, 2, 2, 2], [1, 2, 3, 0]), 4),
    ]
    for _, ((forward, backward, queries), expected) in enumerate(test_cases):
        assert Solution().minTotalTime(forward, backward, queries) == expected
