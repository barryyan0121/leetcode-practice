class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        trie = {}
        for word in words:
            node = trie
            for character in word:
                node = node.setdefault(character, {})

        matches = [0] * len(target)
        for start in range(len(target)):
            node = trie
            for end in range(start, len(target)):
                node = node.get(target[end])
                if node is None:
                    break
                matches[start] += 1

        count = 0
        current_end = farthest = 0
        for index in range(len(target)):
            if index > farthest:
                return -1
            farthest = max(farthest, index + matches[index])
            if index == current_end:
                if farthest == current_end:
                    return -1
                current_end = farthest
                count += 1
                if current_end >= len(target):
                    return count
        return -1


if __name__ == "__main__":
    test_cases = [
        ((["abc", "aaaaa", "bcdef"], "aabcdabc"), 3),
        ((["abababab", "ab"], "ababaababa"), 2),
        ((["abcdef"], "xyz"), -1),
    ]
    for _, ((words, target), expected) in enumerate(test_cases):
        assert Solution().minValidStrings(words, target) == expected
