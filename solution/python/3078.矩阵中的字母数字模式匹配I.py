from typing import List


class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        m, n = len(board), len(board[0])
        h, w = len(pattern), len(pattern[0])
        for r in range(m - h + 1):
            for c in range(n - w + 1):
                mapping, used = {}, set()
                ok = True
                for i in range(h):
                    for j in range(w):
                        ch, value = pattern[i][j], board[r + i][c + j]
                        if ch.isdigit():
                            ok = ok and int(ch) == value
                        elif ch in mapping:
                            ok = ok and mapping[ch] == value
                        elif value in used:
                            ok = False
                        else:
                            mapping[ch] = value
                            used.add(value)
                        if not ok:
                            break
                    if not ok:
                        break
                if ok:
                    return [r, c]
        return [-1, -1]


if __name__ == "__main__":
    s = Solution()
    assert s.findPattern([[1, 2, 2], [2, 2, 3], [2, 3, 3]], ["ab", "bb"]) == [0, 0]
    assert s.findPattern([[1, 1, 2], [3, 3, 4], [6, 6, 6]], ["ab", "66"]) == [1, 1]
    assert s.findPattern([[1, 2], [2, 1]], ["xx"]) == [-1, -1]
    print("3078 ok")
