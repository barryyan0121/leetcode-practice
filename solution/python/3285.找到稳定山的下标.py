class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        return [
            index for index in range(1, len(height)) if height[index - 1] > threshold
        ]


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 4, 5], 2), [3, 4]),
        (([10, 1, 10, 1, 10], 3), [1, 3]),
        (([10, 1, 10, 1, 10], 10), []),
    ]
    for _, ((height, threshold), expected) in enumerate(test_cases):
        assert Solution().stableMountains(height, threshold) == expected
