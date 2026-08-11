"""3104. 查找最长的自包含子串"""


class Solution:
    def maxSubstringLength(self, s: str) -> int:
        first = [len(s)] * 26
        last = [-1] * 26
        for index, char in enumerate(s):
            value = ord(char) - 97
            first[value] = min(first[value], index)
            last[value] = index
        answer = -1
        for left in first:
            if left == len(s):
                continue
            right = left
            valid = True
            for index in range(left, len(s)):
                value = ord(s[index]) - 97
                if first[value] < left:
                    valid = False
                    break
                right = max(right, last[value])
                if valid and right == index and index + 1 < len(s):
                    answer = max(answer, index - left + 1)
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSubstringLength("abba") == 2
    assert solution.maxSubstringLength("abab") == -1
    assert solution.maxSubstringLength("abacd") == 4
