class Solution:
    def minFlips(self, s: str) -> int:
        doubled = s + s
        mismatch_zero = mismatch_one = 0
        answer = 10**9
        for index, char in enumerate(doubled):
            mismatch_zero += char != ("0" if index % 2 == 0 else "1")
            mismatch_one += char != ("1" if index % 2 == 0 else "0")
            if index >= len(s):
                old = doubled[index - len(s)]
                old_index = index - len(s)
                mismatch_zero -= old != ("0" if old_index % 2 == 0 else "1")
                mismatch_one -= old != ("1" if old_index % 2 == 0 else "0")
            if index >= len(s) - 1:
                answer = min(answer, mismatch_zero, mismatch_one)
        return answer
