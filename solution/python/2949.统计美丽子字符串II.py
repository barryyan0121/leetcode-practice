from math import isqrt


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        period = 2 * isqrt(k)
        while period * period % (4 * k):
            period += 1
        count = {(0, 0): 1}
        balance = 0
        answer = 0
        for index, char in enumerate(s, 1):
            balance += 1 if char in vowels else -1
            key = (balance, index % period)
            answer += count.get(key, 0)
            count[key] = count.get(key, 0) + 1
        return answer


assert Solution().beautifulSubstrings("baeyh", 2) == 2
