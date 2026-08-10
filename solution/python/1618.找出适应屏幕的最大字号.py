class Solution:
    def maxFont(
        self, text: str, w: int, h: int, fonts: list[int], fontInfo: "FontInfo"
    ) -> int:
        def fits(size: int) -> bool:
            if fontInfo.getHeight(size) > h:
                return False
            return sum(fontInfo.getWidth(size, ch) for ch in text) <= w

        left, right = 0, len(fonts) - 1
        answer = -1
        while left <= right:
            middle = (left + right) // 2
            if fits(fonts[middle]):
                answer = fonts[middle]
                left = middle + 1
            else:
                right = middle - 1
        return answer


if __name__ == "__main__":

    class FontInfo:
        def getWidth(self, fontSize: int, ch: str) -> int:
            return fontSize + 1

        def getHeight(self, fontSize: int) -> int:
            return fontSize

    test_cases = [
        ("helloworld", 80, 20, [6, 8, 10, 12, 14, 16, 18, 24, 36], 6),
        ("leetcode", 1000, 50, [1, 2, 4], 4),
        ("easyquestion", 100, 100, [10, 15, 20, 25], -1),
    ]
    solution = Solution()
    font_info = FontInfo()
    for index, (text, width, height, fonts, expected) in enumerate(test_cases):
        result = solution.maxFont(text, width, height, fonts, font_info)
        assert result == expected, f"case {index}: {result} != {expected}"
