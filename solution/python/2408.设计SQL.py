"""2408. 设计 SQL"""


class SQL:
    def __init__(self, names: list[str], columns: list[int]):
        self.tables = {name: {} for name in names}
        self.next_id = {name: 1 for name in names}
        self.width = dict(zip(names, columns))

    def ins(self, name: str, row: list[str]) -> bool:
        if name not in self.tables or len(row) != self.width[name]:
            return False
        row_id = self.next_id[name]
        self.next_id[name] += 1
        self.tables[name][row_id] = row[:]
        return True

    def rmv(self, name: str, rowId: int, columnId: int | None = None) -> None:
        if name in self.tables:
            self.tables[name].pop(rowId, None)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or rowId not in self.tables[name]:
            return "<null>"
        row = self.tables[name][rowId]
        if not 1 <= columnId <= len(row):
            return "<null>"
        return row[columnId - 1]

    def exp(self, name: str) -> list[str]:
        if name not in self.tables:
            return []
        return [
            f"{row_id}," + ",".join(row) for row_id, row in self.tables[name].items()
        ]


if __name__ == "__main__":
    test_cases = [((), None)]
    for _, (args, expected) in enumerate(test_cases):
        sql = SQL(["one"], [2])
        assert sql.ins("one", ["a", "b"])
        assert sql.sel("one", 1, 2) == "b"
        sql.rmv("one", 1)
        assert sql.exp("one") == []
