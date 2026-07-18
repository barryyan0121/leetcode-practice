class Solution:
    def longestDupSubstring(self, s: str) -> str:
        length = len(s)
        rank = [ord(char) for char in s]
        suffixes = list(range(length))
        step = 1
        while step < length:
            suffixes.sort(
                key=lambda index: (
                    rank[index],
                    rank[index + step] if index + step < length else -1,
                )
            )
            next_rank = [0] * length
            for index in range(1, length):
                previous, current = suffixes[index - 1], suffixes[index]
                next_rank[current] = next_rank[previous] + (
                    (
                        rank[previous],
                        rank[previous + step] if previous + step < length else -1,
                    )
                    != (
                        rank[current],
                        rank[current + step] if current + step < length else -1,
                    )
                )
            rank = next_rank
            if rank[suffixes[-1]] == length - 1:
                break
            step *= 2
        best = common = 0
        answer = 0
        position = [0] * length
        for index, suffix in enumerate(suffixes):
            position[suffix] = index
        for index in range(length):
            if position[index] == length - 1:
                common = 0
                continue
            other = suffixes[position[index] + 1]
            while (
                index + common < length
                and other + common < length
                and s[index + common] == s[other + common]
            ):
                common += 1
            if common > best:
                best, answer = common, index
            common = max(0, common - 1)
        return s[answer : answer + best]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [("banana", "ana"), ("abcd", ""), ("aaaaa", "aaaa")]
    for _, (text, expected) in enumerate(test_cases):
        assert solution.longestDupSubstring(text) == expected
