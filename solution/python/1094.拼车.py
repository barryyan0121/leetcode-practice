class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        changes = [0] * 1001
        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers
        current = 0
        for change in changes:
            current += change
            if current > capacity:
                return False
        return True


if __name__ == "__main__":
    test_cases = [
        ([[2, 1, 5], [3, 3, 7]], 4, False),
        ([[2, 1, 5], [3, 3, 7]], 5, True),
        ([[2, 1, 5], [3, 5, 7]], 3, True),
        ([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11, True),
        ([[1, 0, 1000]], 1, True),
    ]
    for _, (trips, capacity, expected) in enumerate(test_cases):
        assert Solution().carPooling(trips, capacity) == expected
