class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        answer = current = kinds = 0
        previous = ""
        for char in word:
            if char < previous:
                current = 0
                kinds = 0
            if char != previous:
                kinds += 1
            current += 1
            if kinds == 5:
                answer = max(answer, current)
            previous = char
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu") == 13
    assert solution.longestBeautifulSubstring("aeeeiiiioooauuuuaeiou") == 5
    print("1839 passed")
