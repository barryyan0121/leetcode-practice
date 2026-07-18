class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        changes = [0] * (n + 1)
        for first, last, seats in bookings:
            changes[first - 1] += seats
            changes[last] -= seats
        for index in range(1, n):
            changes[index] += changes[index - 1]
        return changes[:n]


if __name__ == "__main__":
    test_cases = [
        ([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5, [10, 55, 45, 25, 25]),
        ([[1, 2, 10], [2, 2, 15]], 2, [10, 25]),
        ([[1, 1, 7]], 1, [7]),
    ]
    for _, (bookings, n, expected) in enumerate(test_cases):
        assert Solution().corpFlightBookings(bookings, n) == expected
