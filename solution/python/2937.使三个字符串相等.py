"""2937. 使三个字符串相等"""


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        common = 0
        while (
            common < min(len(s1), len(s2), len(s3))
            and s1[common] == s2[common] == s3[common]
        ):
            common += 1
        return -1 if common == 0 else len(s1) + len(s2) + len(s3) - 3 * common


if __name__ == "__main__":
    assert Solution().findMinimumOperations("abc", "abb", "ab") == 2
