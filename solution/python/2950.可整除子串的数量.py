class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        groups = ["ab", "cde", "fgh", "ijk", "lmn", "opq", "rst", "uvw", "xyz"]
        values = {
            char: digit for digit, group in enumerate(groups, 1) for char in group
        }
        answer = 0
        for left in range(len(word)):
            total = 0
            for right in range(left, len(word)):
                total += values[word[right]]
                length = right - left + 1
                if total % length == 0:
                    answer += 1
        return answer


assert Solution().countDivisibleSubstrings("asdf") == 6
