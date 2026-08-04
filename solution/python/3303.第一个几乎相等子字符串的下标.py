class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def z_function(text: str) -> list[int]:
            values = [0] * len(text)
            left = right = 0
            for index in range(1, len(text)):
                if index <= right:
                    values[index] = min(right - index + 1, values[index - left])
                while (
                    index + values[index] < len(text)
                    and text[values[index]] == text[index + values[index]]
                ):
                    values[index] += 1
                if index + values[index] - 1 > right:
                    left, right = index, index + values[index] - 1
            return values

        size = len(pattern)
        prefix = z_function(pattern + "#" + s)
        suffix = z_function(pattern[::-1] + "#" + s[::-1])
        for start in range(len(s) - size + 1):
            prefix_length = min(prefix[size + 1 + start], size)
            reverse_start = len(s) - (start + size)
            suffix_length = min(suffix[size + 1 + reverse_start], size)
            if prefix_length + suffix_length >= size - 1:
                return start
        return -1


if __name__ == "__main__":
    test_cases = [
        (("abcdefg", "bcdffg"), 1),
        (("ababbab", "babba"), 1),
        (("aaaa", "bbb"), -1),
    ]
    for _, ((s, pattern), expected) in enumerate(test_cases):
        assert Solution().minStartingIndex(s, pattern) == expected
