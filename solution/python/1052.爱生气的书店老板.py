class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        base = sum(customer for customer, bad in zip(customers, grumpy) if not bad)
        extra = best = 0
        for i, (customer, bad) in enumerate(zip(customers, grumpy)):
            extra += customer * bad
            if i >= minutes:
                extra -= customers[i - minutes] * grumpy[i - minutes]
            best = max(best, extra)
        return base + best


if __name__ == "__main__":
    test_cases = [([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3, 16)]
    for _, (customers, grumpy, minutes, expected) in enumerate(test_cases):
        assert Solution().maxSatisfied(customers, grumpy, minutes) == expected
