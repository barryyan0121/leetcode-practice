"""1915. 最美子字符串的数目"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counts = [0] * (1 << 10)
        counts[0] = 1
        mask = 0
        answer = 0
        for char in word:
            mask ^= 1 << (ord(char) - 97)
            answer += counts[mask]
            for bit in range(10):
                answer += counts[mask ^ (1 << bit)]
            counts[mask] += 1
        return answer


if __name__ == "__main__":
    test_cases = [("aba", 4), ("aabb", 9)]
    for _, (word, expected) in enumerate(test_cases):
        assert Solution().wonderfulSubstrings(word) == expected
