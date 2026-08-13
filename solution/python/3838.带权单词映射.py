from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join(
            chr(ord("z") - sum(weights[ord(char) - ord("a")] for char in word) % 26)
            for word in words
        )


if __name__ == "__main__":
    assert Solution().mapWordWeights(["a", "b", "c"], [1] * 26) == "yyy"
