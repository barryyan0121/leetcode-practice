class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        result = [0] * num_people
        gift = 1
        while candies:
            amount = min(candies, gift)
            result[(gift - 1) % num_people] += amount
            candies -= amount
            gift += 1
        return result


if __name__ == "__main__":
    test_cases = [
        (7, 4, [1, 2, 3, 1]),
        (10, 3, [5, 2, 3]),
        (1, 1, [1]),
        (60, 4, [15, 18, 15, 12]),
    ]
    for _, (candies, num_people, expected) in enumerate(test_cases):
        assert Solution().distributeCandies(candies, num_people) == expected
