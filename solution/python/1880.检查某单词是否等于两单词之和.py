class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def value(word: str) -> int:
            result = 0
            for char in word:
                result = result * 10 + ord(char) - 97
            return result

        return value(firstWord) + value(secondWord) == value(targetWord)


if __name__ == "__main__":
    solution = Solution()
    assert solution.isSumEqual("acb", "cba", "cdb") is True
    print("1880 passed")
