class Solution:
    def differByOne(self, dict: list[str]) -> bool:
        length = len(dict[0])
        base, mod1, mod2 = 27, 1_000_000_007, 1_000_000_009
        powers1, powers2 = [1] * (length + 1), [1] * (length + 1)
        for index in range(length):
            powers1[index + 1] = powers1[index] * base % mod1
            powers2[index + 1] = powers2[index] * base % mod2
        prefixes = []
        for word in dict:
            first, second = [0], [0]
            for char in word:
                value = ord(char) - 96
                first.append((first[-1] * base + value) % mod1)
                second.append((second[-1] * base + value) % mod2)
            prefixes.append((first, second))
        for index in range(length):
            seen = set()
            tail = length - index - 1
            for first, second in prefixes:
                pattern = (
                    (
                        first[index] * powers1[tail]
                        + first[-1]
                        - first[index + 1] * powers1[tail]
                    )
                    % mod1,
                    (
                        second[index] * powers2[tail]
                        + second[-1]
                        - second[index + 1] * powers2[tail]
                    )
                    % mod2,
                )
                if pattern in seen:
                    return True
                seen.add(pattern)
        return False


if __name__ == "__main__":
    test_cases = [(["abcd", "acbd", "aacd"], True), (["ab", "cd", "yz"], False)]
    for _, (words, expected) in enumerate(test_cases):
        assert Solution().differByOne(words) == expected
