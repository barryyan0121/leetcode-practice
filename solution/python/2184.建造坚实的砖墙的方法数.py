"""2184. 建造坚实的砖墙的方法数"""


class Solution:
    def buildWall(self, height: int, width: int, bricks: list[int]) -> int:
        modulus = 10**9 + 7
        masks = []

        def generate(position: int, mask: int) -> None:
            if position == width:
                masks.append(mask)
                return
            for brick in bricks:
                if position + brick <= width:
                    generate(
                        position + brick,
                        (
                            mask | (1 << (position + brick))
                            if position + brick < width
                            else mask
                        ),
                    )

        generate(0, 0)
        compatible = {
            mask: [other for other in masks if not mask & other] for mask in masks
        }
        ways = {mask: 1 for mask in masks}
        for _ in range(1, height):
            ways = {
                mask: sum(ways[other] for other in compatible[mask]) % modulus
                for mask in masks
            }
        return sum(ways.values()) % modulus


if __name__ == "__main__":
    assert Solution().buildWall(2, 3, [1, 2]) == 2
