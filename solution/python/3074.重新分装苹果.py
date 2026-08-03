class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total = sum(apple)
        used = 0
        for count, size in enumerate(sorted(capacity, reverse=True), 1):
            used += size
            if used >= total:
                return count
        return len(capacity)


if __name__ == "__main__":
    test_cases = [(([1, 3], [2, 2, 4, 3]), 1), (([5, 5, 5], [2, 4, 2, 7]), 4)]
    for _, ((apple, capacity), expected) in enumerate(test_cases):
        assert Solution().minimumBoxes(apple, capacity) == expected
