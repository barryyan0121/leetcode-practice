"""3298. 统计可重新排列包含另一个字符串 II 的子字符串数目"""


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        need = [0] * 26
        for char in word2:
            need[ord(char) - ord("a")] += 1

        missing = len(word2)
        answer = 0
        left = 0
        for right, char in enumerate(word1):
            index = ord(char) - ord("a")
            need[index] -= 1
            if need[index] >= 0:
                missing -= 1
            while missing == 0:
                answer += len(word1) - right
                left_index = ord(word1[left]) - ord("a")
                need[left_index] += 1
                if need[left_index] > 0:
                    missing += 1
                left += 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (("bcca", "abc"), 1),
        (("abcabc", "abc"), 10),
        (("abcabc", "aaabc"), 0),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().validSubstringCount(*args) == expected
