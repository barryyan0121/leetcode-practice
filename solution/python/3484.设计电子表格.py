"""3484. 设计电子表格"""


class Spreadsheet:
    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells.pop(cell, None)

    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split("+")
        return self._value(left) + self._value(right)

    def _value(self, operand: str) -> int:
        return int(operand) if operand.isdigit() else self.cells.get(operand, 0)


test_cases = [
    (
        3,
        [
            ("getValue", "=5+7"),
            ("setCell", "A1", 10),
            ("getValue", "=A1+6"),
            ("setCell", "B2", 15),
            ("getValue", "=A1+B2"),
            ("resetCell", "A1"),
            ("getValue", "=A1+B2"),
        ],
        [12, None, 16, None, 25, None, 15],
    )
]


if __name__ == "__main__":
    for _, (rows, operations, expected) in enumerate(test_cases):
        spreadsheet = Spreadsheet(rows)
        actual = []
        for operation in operations:
            method = getattr(spreadsheet, operation[0])
            actual.append(method(*operation[1:]))
        assert actual == expected
