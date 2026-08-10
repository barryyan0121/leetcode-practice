"""2271. 毯子覆盖的最多白色砖块数"""


class Solution:
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        tiles.sort()
        left = covered = answer = 0
        for right, (start, end) in enumerate(tiles):
            covered += end - start + 1
            while tiles[left][1] < end - carpetLen + 1:
                covered -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            window_start = end - carpetLen + 1
            window_end = end
            if left == right:
                overlap = max(0, min(end, window_end) - max(start, window_start) + 1)
                covered_in_window = overlap
            else:
                covered_in_window = covered
                covered_in_window -= max(0, window_start - tiles[left][0])
                covered_in_window -= max(0, end - window_end)
            answer = max(answer, covered_in_window)
        return answer
