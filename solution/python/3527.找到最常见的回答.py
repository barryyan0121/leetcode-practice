from collections import Counter


class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        counts = Counter()
        for response in responses:
            counts.update(set(response))
        return min(counts, key=lambda value: (-counts[value], value))


if __name__ == "__main__":
    test_cases = [
        (
            (
                [
                    ["good", "ok", "good", "ok"],
                    ["ok", "bad", "good", "ok", "ok"],
                    ["good"],
                    ["bad"],
                ],
            ),
            "good",
        ),
        (
            (
                [
                    ["good", "ok", "good"],
                    ["ok", "bad"],
                    ["bad", "notsure"],
                    ["great", "good"],
                ],
            ),
            "bad",
        ),
    ]
    for _, ((responses,), expected) in enumerate(test_cases):
        assert Solution().findCommonResponse(responses) == expected
