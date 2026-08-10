"""3035. 最多可以被 K 个回文串覆盖的单词"""

from collections import Counter


class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        counts = Counter("".join(words))
        pairs = sum(value // 2 for value in counts.values())
        singles = sum(value % 2 for value in counts.values())
        answer = 0
        for length in sorted(map(len, words)):
            need = length // 2
            if pairs < need:
                break
            pairs -= need
            if length % 2:
                if singles:
                    singles -= 1
                elif pairs:
                    pairs -= 1
                    singles = 1
                else:
                    break
            answer += 1
        return answer


if __name__ == "__main__":
    assert Solution().maxPalindromesAfterOperations(["abbb", "cc"]) == 1
