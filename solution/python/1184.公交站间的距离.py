from typing import List


class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        if start > destination:
            start, destination = destination, start
        clockwise = sum(distance[start:destination])
        return min(clockwise, sum(distance) - clockwise)


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4], 0, 1, 1), ([1, 2, 3, 4], 0, 2, 3)]
    for _, (distance, start, destination, expected) in enumerate(test_cases):
        assert (
            Solution().distanceBetweenBusStops(distance, start, destination) == expected
        )
