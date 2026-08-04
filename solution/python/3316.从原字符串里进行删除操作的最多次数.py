from bisect import bisect_left


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: list[int]) -> int:
        length = len(pattern)
        suffix_matches = [0] * (len(source) + 1)
        for index in range(len(source) - 1, -1, -1):
            suffix_matches[index] = suffix_matches[index + 1]
            if (
                suffix_matches[index + 1] < length
                and source[index] == pattern[length - suffix_matches[index + 1] - 1]
            ):
                suffix_matches[index] += 1

        removable = set(targetIndices)
        target_positions = [[] for _ in range(26)]
        fixed_positions = [[] for _ in range(26)]
        for index, character in enumerate(source):
            positions = target_positions if index in removable else fixed_positions
            positions[ord(character) - ord("a")].append(index)

        source_index = 0
        kept_removable = 0
        for pattern_index, character in enumerate(pattern):
            remaining = length - pattern_index - 1
            bucket = ord(character) - ord("a")
            fixed = fixed_positions[bucket]
            target = target_positions[bucket]
            fixed_offset = bisect_left(fixed, source_index)
            if (
                fixed_offset < len(fixed)
                and suffix_matches[fixed[fixed_offset] + 1] >= remaining
            ):
                source_index = fixed[fixed_offset] + 1
                continue
            target_offset = bisect_left(target, source_index)
            if (
                target_offset == len(target)
                or suffix_matches[target[target_offset] + 1] < remaining
            ):
                return 0
            source_index = target[target_offset] + 1
            kept_removable += 1
        return len(targetIndices) - kept_removable


if __name__ == "__main__":
    test_cases = [
        (("abc", "abc", [0, 1, 2]), 0),
        (("abcab", "abc", [0, 1, 2, 3, 4]), 2),
        (("abbaa", "aba", [0, 1, 2]), 1),
    ]
    for _, ((source, pattern, target_indices), expected) in enumerate(test_cases):
        assert Solution().maxRemovals(source, pattern, target_indices) == expected
