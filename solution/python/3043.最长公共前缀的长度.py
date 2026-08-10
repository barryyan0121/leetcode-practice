"""3043. 最长公共前缀的长度"""


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes = set()
        for number in arr1:
            text = str(number)
            for end in range(1, len(text) + 1):
                prefixes.add(text[:end])
        return max(
            (
                end
                for number in arr2
                for end in range(1, len(str(number)) + 1)
                if str(number)[:end] in prefixes
            ),
            default=0,
        )


if __name__ == "__main__":
    assert Solution().longestCommonPrefix([1, 10, 100], [1000, 100]) == 3
