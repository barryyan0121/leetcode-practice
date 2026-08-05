"""2137. 通过倒水使水量相等"""


class Solution:
    def equalizeWater(self, buckets: list[int], loss: int) -> float:
        low, high = 0.0, max(buckets)
        efficiency = (100 - loss) / 100
        for _ in range(60):
            middle = (low + high) / 2
            gain = sum(
                (value - middle) * efficiency for value in buckets if value > middle
            )
            need = sum(middle - value for value in buckets if value < middle)
            if gain >= need:
                low = middle
            else:
                high = middle
        return low


if __name__ == "__main__":
    test_cases = [(([1, 2, 7], 80), 2.0)]
    for _, (args, expected) in enumerate(test_cases):
        assert abs(Solution().equalizeWater(*args) - expected) < 1e-5
