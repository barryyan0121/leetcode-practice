"""2024. 考试的最大困扰度"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answer = 0
        for target in "TF":
            left = changes = 0
            for right, value in enumerate(answerKey):
                changes += value != target
                while changes > k:
                    changes -= answerKey[left] != target
                    left += 1
                answer = max(answer, right - left + 1)
        return answer


if __name__ == "__main__":
    test_cases = [(("TTFF", 2), 4), [("TFFT", 1), 3]]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxConsecutiveAnswers(*args) == expected
