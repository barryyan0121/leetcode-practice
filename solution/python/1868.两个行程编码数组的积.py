from typing import List


class Solution:
    def findRLEArray(
        self, encoded1: List[List[int]], encoded2: List[List[int]]
    ) -> List[List[int]]:
        result = []
        i = j = 0
        while i < len(encoded1) and j < len(encoded2):
            value = encoded1[i][0] * encoded2[j][0]
            count = min(encoded1[i][1], encoded2[j][1])
            if result and result[-1][0] == value:
                result[-1][1] += count
            else:
                result.append([value, count])
            encoded1[i][1] -= count
            encoded2[j][1] -= count
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        return result

if __name__ == "__main__":
    assert Solution().findRLEArray([[1, 3], [2, 3]], [[6, 1], [3, 2], [2, 3]]) == [[6, 1], [6, 2], [4, 3]]
