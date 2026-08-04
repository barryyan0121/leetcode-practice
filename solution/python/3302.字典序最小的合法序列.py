class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        length = len(word2)
        exact = [0] * (len(word1) + 1)
        almost = [0] * (len(word1) + 1)
        for index in range(len(word1) - 1, -1, -1):
            exact[index] = exact[index + 1]
            almost[index] = almost[index + 1]
            if exact[index + 1] < length:
                if word1[index] == word2[length - exact[index + 1] - 1]:
                    exact[index] = exact[index + 1] + 1
                almost[index] = max(almost[index], exact[index + 1] + 1)
            if (
                almost[index + 1] < length
                and word1[index] == word2[length - almost[index + 1] - 1]
            ):
                almost[index] = almost[index + 1] + 1

        answer = []
        word2_index = 0
        changed = False
        for index, character in enumerate(word1):
            if word2_index == length:
                break
            remaining = length - word2_index - 1
            can_match = (
                almost[index + 1] >= remaining
                if character == word2[word2_index]
                else not changed and exact[index + 1] >= remaining
            )
            if can_match:
                answer.append(index)
                changed |= character != word2[word2_index]
                word2_index += 1
        return answer if word2_index == length else []


if __name__ == "__main__":
    test_cases = [
        (("vbcca", "abc"), [0, 1, 2]),
        (("bacdc", "abc"), [1, 2, 4]),
        (("aaaaaa", "aaabc"), []),
        (("abc", "ab"), [0, 1]),
    ]
    for _, ((word1, word2), expected) in enumerate(test_cases):
        assert Solution().validSequence(word1, word2) == expected
