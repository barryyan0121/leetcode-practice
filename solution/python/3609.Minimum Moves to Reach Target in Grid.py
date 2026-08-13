class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        result = 0
        while sx != tx or sy != ty:
            if not (sx <= tx and sy <= ty):
                return -1

            if tx < ty:
                if tx > ty - tx:
                    ty -= tx
                else:
                    if ty % 2:
                        return -1
                    ty -= ty // 2
            elif tx > ty:
                if ty > tx - ty:
                    tx -= ty
                else:
                    if tx % 2:
                        return -1
                    tx -= tx // 2
            else:
                if sx == 0:
                    tx -= ty
                elif sy == 0:
                    ty -= tx
                else:
                    return -1
            result += 1

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.minMoves(1, 2, 5, 4) == 2
    assert s.minMoves(0, 1, 2, 3) == 3
    assert s.minMoves(1, 1, 2, 2) == -1
    print("3609 ok")
