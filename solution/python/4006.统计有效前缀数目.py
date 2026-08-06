"""4006. 统计有效前缀数目"""


class Solution:
    def countValidPrefixes(self, s: str) -> int:
        difference = answer = 0
        for character in s:
            difference += 1 if character == "1" else -1
            answer += abs(difference) <= 1
        return answer


if __name__ == "__main__":
    assert Solution().countValidPrefixes("00101") == 3
    assert Solution().countValidPrefixes("101") == 3
