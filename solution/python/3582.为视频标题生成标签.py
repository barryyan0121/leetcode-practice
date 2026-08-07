"""3582. 为视频标题生成标签"""


class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return "#"
        tag = "#" + words[0].lower() + "".join(word.capitalize() for word in words[1:])
        return tag[:100]


if __name__ == "__main__":
    test_cases = [
        (("Leetcode daily streak achieved",), "#leetcodeDailyStreakAchieved"),
        (("can I Go There",), "#canIGoThere"),
        ((" ",), "#"),
    ]
    for _, ((caption,), expected) in enumerate(test_cases):
        assert Solution().generateTag(caption) == expected
