class Solution:
    def sameEndSubstringCount(self, s: str, queries: list[list[int]]) -> list[int]:
        prefix = [[0] * 26]
        for char in s:
            row = prefix[-1][:]
            row[ord(char) - 97] += 1
            prefix.append(row)
        answer = []
        for left, right in queries:
            total = 0
            for index in range(26):
                count = prefix[right + 1][index] - prefix[left][index]
                total += count * (count + 1) // 2
            answer.append(total)
        return answer
