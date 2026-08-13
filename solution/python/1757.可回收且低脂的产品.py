import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[
        (products["low_fats"] == "Y") & (products["recyclable"] == "Y"),
        ["product_id"],
    ]


if __name__ == "__main__":
    test_cases = [
        (
            pd.DataFrame(
                {
                    "product_id": [0, 1, 2, 3, 4],
                    "low_fats": ["Y", "Y", "N", "Y", "N"],
                    "recyclable": ["N", "Y", "Y", "Y", "N"],
                }
            ),
            pd.DataFrame({"product_id": [1, 3]}),
        ),
    ]
    for index, (products, expected) in enumerate(test_cases):
        actual = find_products(products).reset_index(drop=True)
        assert actual.equals(expected), index
