"""2957. 移除相邻近似相等字符"""


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        answer = 0
        index = 1
        while index < len(word):
            if abs(ord(word[index]) - ord(word[index - 1])) <= 1:
                answer += 1
                index += 2
            else:
                index += 1
        return answer


if __name__ == "__main__":
    assert Solution().removeAlmostEqualCharacters("aaaaa") == 2
