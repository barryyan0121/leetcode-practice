#
# @lc app=leetcode.cn id=631 lang=python3
#
# [631] 设计 Excel 求和公式
#


# @lc code=start
class Excel:
    def __init__(self, height: int, width: str):
        self.values = {}
        self.formulas = {}

    def _cell(self, ref):
        return ord(ref[0]) - 65, int(ref[1:])

    def _refs(self, token):
        if ":" not in token:
            yield self._cell(token)
            return
        left, right = token.split(":")
        c1, r1 = self._cell(left)
        c2, r2 = self._cell(right)
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                yield col, row

    def set(self, row: int, column: str, val: int) -> None:
        key = self._cell(column + str(row))
        self.values[key] = val
        self.formulas.pop(key, None)

    def get(self, row: int, column: str) -> int:
        key = self._cell(column + str(row))
        return self._eval(key, {})

    def _eval(self, key, memo):
        if key in memo:
            return memo[key]
        if key in self.formulas:
            value = sum(
                count * self._eval((c, r), memo)
                for (c, r), count in self.formulas[key].items()
            )
        else:
            value = self.values.get(key, 0)
        memo[key] = value
        return value

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        key = self._cell(column + str(row))
        counts = {}
        for token in numbers:
            for ref in self._refs(token):
                counts[ref] = counts.get(ref, 0) + 1
        self.formulas[key] = counts
        self.values.pop(key, None)
        return self.get(row, column)


# @lc code=end


if __name__ == "__main__":
    excel = Excel(3, "C")
    excel.set(1, "A", 2)
    assert excel.get(1, "A") == 2
    assert excel.sum(3, "C", ["A1", "A1:B2"]) == 4
