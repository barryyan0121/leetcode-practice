"""2014. 重复 K 次的最长子序列"""

from collections import Counter


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        counts = Counter(s)
        chars = sorted((c for c, count in counts.items() if count >= k), reverse=True)

        def repeated(candidate: str) -> bool:
            found = repeats = 0
            for char in s:
                if char == candidate[found]:
                    found += 1
                    if found == len(candidate):
                        repeats += 1
                        found = 0
                        if repeats == k:
                            return True
            return False

        answer = ""

        def search(candidate: str) -> None:
            nonlocal answer
            if len(candidate) > len(answer):
                answer = candidate
            if len(candidate) == 7:
                return
            for char in chars:
                trial = candidate + char
                if repeated(trial):
                    search(trial)

        search("")
        return answer


if __name__ == "__main__":
    test_cases = [(("letsleetcode", 2), "let"), (("bb", 2), "b")]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().longestSubsequenceRepeatedK(*args) == expected
