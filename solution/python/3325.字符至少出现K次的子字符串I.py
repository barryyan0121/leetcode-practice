from collections import deque


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        occurrences = [deque() for _ in range(26)]
        latest_start = -1
        answer = 0
        for index, character in enumerate(s):
            positions = occurrences[ord(character) - ord("a")]
            positions.append(index)
            if len(positions) > k:
                positions.popleft()
            if len(positions) == k:
                latest_start = max(latest_start, positions[0])
            answer += latest_start + 1
        return answer


if __name__ == "__main__":
    test_cases = [
        (("abacb", 2), 4),
        (("abcde", 1), 15),
        (("a", 2), 0),
    ]
    for _, ((s, k), expected) in enumerate(test_cases):
        assert Solution().numberOfSubstrings(s, k) == expected
