class Solution:
    def minimizeConcatenatedLength(self, words: list[str]) -> int:
        dp = {(words[0][0], words[0][-1]): len(words[0])}
        for word in words[1:]:
            nxt = {}
            for (first, last), length in dp.items():
                nxt[(first, word[-1])] = min(
                    nxt.get((first, word[-1]), 10**9),
                    length + len(word) - (last == word[0]),
                )
                nxt[(word[0], last)] = min(
                    nxt.get((word[0], last), 10**9),
                    length + len(word) - (word[-1] == first),
                )
            dp = nxt
        return min(dp.values())


if __name__ == "__main__":
    assert Solution().minimizeConcatenatedLength(["aa", "ab", "bc"]) == 4
