"""2217. 找到指定长度的回文数"""


class Solution:
    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        half = (intLength + 1) // 2
        start = 10 ** (half - 1)
        limit = 10**half - start
        answer = []
        for query in queries:
            value = start + query - 1
            if query > limit:
                answer.append(-1)
                continue
            text = str(value)
            answer.append(int(text + text[-1 - (intLength % 2) :: -1]))
        return answer
