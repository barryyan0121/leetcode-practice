class Solution:
    def minimizeError(self, prices: list[str], target: int) -> str:
        cents = [int(price.replace(".", "")) for price in prices]
        floors = [price // 1000 for price in cents]
        need = target - sum(floors)
        fractions = sorted(
            (price % 1000 for price in cents if price % 1000), reverse=True
        )
        if need < 0 or need > len(fractions):
            return "-1"
        error = sum(fractions)
        for fraction in fractions[:need]:
            error += 1000 - 2 * fraction
        return f"{error // 1000}.{error % 1000:03d}"


if __name__ == "__main__":
    test_cases = [(["0.700", "2.800", "4.900"], 8, "1.000"), (["1.000"], 2, "-1")]
    for _, (prices, target, expected) in enumerate(test_cases):
        assert Solution().minimizeError(prices, target) == expected
