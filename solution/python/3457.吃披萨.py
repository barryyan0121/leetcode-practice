class Solution:
    def maxWeight(self, pizzas: list[int]) -> int:
        draxemilon = pizzas
        pizzas.sort()
        days = len(pizzas) // 4
        odd = (days + 1) // 2
        even = days // 2
        left, right = 0, len(pizzas) - 1
        answer = 0
        for _ in range(odd):
            answer += pizzas[right]
            right -= 1
            left += 3
        for _ in range(even):
            answer += pizzas[right - 1]
            right -= 2
            left += 2
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5, 6, 7, 8],), 14),
        (([2, 1, 1, 1, 1, 1, 1, 1],), 3),
    ]
    for _, ((pizzas,), expected) in enumerate(test_cases):
        assert Solution().maxWeight(pizzas) == expected
