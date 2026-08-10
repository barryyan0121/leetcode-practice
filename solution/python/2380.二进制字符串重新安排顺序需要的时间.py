"""2380. 二进制字符串重新安排顺序需要的时间"""


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeros = answer = 0
        for char in s:
            if char == "0":
                zeros += 1
            elif zeros:
                answer = max(answer + 1, zeros)
        return answer
