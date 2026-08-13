import pandas as pd
from pandas.testing import assert_frame_equal


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values("weight", ascending=False)[
        ["name"]
    ]


class Solution:
    def findHeavyAnimals(self, animals: pd.DataFrame) -> pd.DataFrame:
        return findHeavyAnimals(animals)


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame(
                {
                    "name": ["Tatiana", "Khaled", "Alex", "Jonathan"],
                    "species": ["Snake", "Giraffe", "Leopard", "Monkey"],
                    "age": [98, 50, 6, 45],
                    "weight": [464, 41, 328, 463],
                }
            ),
            pd.DataFrame({"name": ["Tatiana", "Jonathan", "Alex"]}),
        )
    ]

    solver = Solution()
    for index, (animals, expected) in enumerate(test_cases):
        actual = solver.findHeavyAnimals(animals.copy())
        assert_frame_equal(actual.reset_index(drop=True), expected), (
            f"case {index} failed"
        )
