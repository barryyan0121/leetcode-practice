"""2166. 设计位集"""


class Bitset:
    def __init__(self, size: int):
        self.bits = [0] * size
        self.flipped = False

    def fix(self, idx: int) -> None:
        self.bits[idx] = int(not self.flipped)

    def unfix(self, idx: int) -> None:
        self.bits[idx] = int(self.flipped)

    def flip(self) -> None:
        self.flipped = not self.flipped

    def all(self) -> bool:
        return all(self.bits) if not self.flipped else not any(self.bits)

    def one(self) -> bool:
        return any(self.bits) if not self.flipped else not all(self.bits)

    def count(self) -> int:
        return sum(self.bits) if not self.flipped else len(self.bits) - sum(self.bits)

    def toString(self) -> str:
        return "".join(str(value ^ self.flipped) for value in self.bits)


if __name__ == "__main__":
    test_cases = [(3, "000")]
    for _, (size, expected) in enumerate(test_cases):
        assert Bitset(size).toString() == expected
