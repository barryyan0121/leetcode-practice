class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length = len(word)
        z = [0] * length
        left = right = 0
        for index in range(1, length):
            if index <= right:
                z[index] = min(right - index + 1, z[index - left])
            while (
                index + z[index] < length and word[z[index]] == word[index + z[index]]
            ):
                z[index] += 1
            if index + z[index] - 1 > right:
                left, right = index, index + z[index] - 1
        for time in range(k, length, k):
            if z[time] >= length - time:
                return time // k
        return (length + k - 1) // k


if __name__ == "__main__":
    test_cases = [(("abacaba", 3), 2), (("abacaba", 4), 1), (("abcbabcd", 2), 4)]
    for _, ((word, k), expected) in enumerate(test_cases):
        assert Solution().minimumTimeToInitialState(word, k) == expected
