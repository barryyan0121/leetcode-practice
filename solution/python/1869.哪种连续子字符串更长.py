class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        best = [0, 0]
        current = [0, 0]
        for char in s:
            index = int(char)
            current[index] += 1
            current[1 - index] = 0
            best[index] = max(best[index], current[index])
        return best[1] > best[0]
