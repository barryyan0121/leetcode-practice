class Solution:
    def shortestSubstrings(self, arr: list[str]) -> list[str]:
        answer = []
        for index, word in enumerate(arr):
            candidates = []
            for length in range(1, len(word) + 1):
                for start in range(len(word) - length + 1):
                    candidate = word[start : start + length]
                    if all(
                        candidate not in other
                        for other_index, other in enumerate(arr)
                        if other_index != index
                    ):
                        candidates.append(candidate)
                if candidates:
                    answer.append(min(candidates))
                    break
            else:
                answer.append("")
        return answer


if __name__ == "__main__":
    test_cases = [
        (["cab", "ad", "bad", "c"], ["ab", "", "ba", ""]),
        (["abc", "bcd", "abcd"], ["", "", "abcd"]),
    ]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().shortestSubstrings(arr) == expected
