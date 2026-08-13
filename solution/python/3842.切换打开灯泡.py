from typing import List


class Solution:
    def toggleLightBulbs(self, bulbs: List[int]) -> List[int]:
        state = set()
        for bulb in bulbs:
            if bulb in state:
                state.remove(bulb)
            else:
                state.add(bulb)
        return sorted(state)


if __name__ == "__main__":
    assert Solution().toggleLightBulbs([1, 2, 1, 2, 3]) == [3]
