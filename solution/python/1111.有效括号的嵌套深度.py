class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        answer = []
        for char in seq:
            if char == "(":
                depth += 1
                answer.append(depth % 2)
            else:
                answer.append(depth % 2)
                depth -= 1
        return answer


if __name__ == "__main__":
    test_cases = [("(()())", [1, 0, 0, 0, 0, 1])]
    for _, (seq, expected) in enumerate(test_cases):
        assert Solution().maxDepthAfterSplit(seq) == expected
