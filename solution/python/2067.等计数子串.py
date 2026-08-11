class Solution:
    def equalCountSubstrings(self, s, count):
        answer = 0
        for unique in range(1, 27):
            length = unique * count
            if length > len(s):
                break
            freq = [0] * 26
            for i, char in enumerate(s):
                freq[ord(char) - 97] += 1
                if i >= length:
                    freq[ord(s[i - length]) - 97] -= 1
                if (
                    i >= length - 1
                    and sum(x > 0 for x in freq) == unique
                    and max(freq) == count
                ):
                    answer += 1
        return answer
