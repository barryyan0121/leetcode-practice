class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:
        minimum = -1
        maximum = total = sum_values = mode = max_frequency = 0
        for value, frequency in enumerate(count):
            if frequency:
                if minimum == -1:
                    minimum = value
                maximum = value
                total += frequency
                sum_values += value * frequency
                if frequency > max_frequency:
                    mode = value
                    max_frequency = frequency

        first_rank, second_rank = (total + 1) // 2, (total + 2) // 2
        cumulative = 0
        first_median = second_median = 0
        found_first = False
        for value, frequency in enumerate(count):
            cumulative += frequency
            if cumulative >= first_rank and not found_first:
                first_median = value
                found_first = True
            if cumulative >= second_rank:
                second_median = value
                break
        return [
            float(minimum),
            float(maximum),
            sum_values / total,
            (first_median + second_median) / 2,
            float(mode),
        ]


if __name__ == "__main__":
    test_cases = [
        ([0, 1, 3, 4, 0, 0], [1.0, 3.0, 2.375, 2.5, 3.0]),
        ([1] + [0] * 254 + [1], [0.0, 255.0, 127.5, 127.5, 0.0]),
        ([0] * 42 + [5], [42.0, 42.0, 42.0, 42.0, 42.0]),
    ]
    for _, (count, expected) in enumerate(test_cases):
        assert Solution().sampleStats(count) == expected
