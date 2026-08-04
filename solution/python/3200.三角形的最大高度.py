class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def height(first: int, second: int) -> int:
            level = 1
            while True:
                if level % 2:
                    first -= level
                else:
                    second -= level
                if first < 0 or second < 0:
                    return level - 1
                level += 1

        return max(height(red, blue), height(blue, red))


if __name__ == "__main__":
    test_cases = [((2, 4), 3), ((2, 1), 2), ((1, 1), 1), ((10, 1), 2)]
    for _, ((red, blue), expected) in enumerate(test_cases):
        assert Solution().maxHeightOfTriangle(red, blue) == expected
