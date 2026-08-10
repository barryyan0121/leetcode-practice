from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        available = {""}
        answer = ""
        for word in sorted(words, key=lambda value: (len(value), value)):
            if word[:-1] in available:
                available.add(word)
                if len(word) > len(answer):
                    answer = word
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestWord(["w", "wo", "wor", "worl", "world"]) == "world"
    print("1858 passed")
