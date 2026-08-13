from bisect import bisect_left
from typing import List


class Solution:
    def closestRoom(
        self, rooms: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        rooms.sort(key=lambda room: room[1], reverse=True)
        room_ids = sorted(room[0] for room in rooms)
        size = 1
        while size < len(room_ids):
            size <<= 1
        tree = [0] * (2 * size)

        def activate(index: int) -> None:
            index += size
            tree[index] = 1
            index //= 2
            while index:
                tree[index] = tree[index * 2] + tree[index * 2 + 1]
                index //= 2

        def find_first(node: int, left: int, right: int, target: int) -> int:
            if right <= target or tree[node] == 0:
                return -1
            if right - left == 1:
                return left
            middle = (left + right) // 2
            result = find_first(node * 2, left, middle, target)
            return (
                result
                if result >= 0
                else find_first(node * 2 + 1, middle, right, target)
            )

        def find_last(node: int, left: int, right: int, target: int) -> int:
            if left > target or tree[node] == 0:
                return -1
            if right - left == 1:
                return left
            middle = (left + right) // 2
            result = find_last(node * 2 + 1, middle, right, target)
            return result if result >= 0 else find_last(node * 2, left, middle, target)

        room_index = 0
        answer = [-1] * len(queries)
        pending = sorted(enumerate(queries), key=lambda item: item[1][1], reverse=True)
        for index, (preferred, minimum) in pending:
            while room_index < len(rooms) and rooms[room_index][1] >= minimum:
                activate(bisect_left(room_ids, rooms[room_index][0]))
                room_index += 1
            position = bisect_left(room_ids, preferred)
            successor = find_first(1, 0, size, position)
            predecessor = find_last(1, 0, size, position - 1)
            candidates = []
            if successor >= 0 and successor < len(room_ids):
                candidates.append(room_ids[successor])
            if predecessor >= 0:
                candidates.append(room_ids[predecessor])
            if candidates:
                answer[index] = min(
                    candidates, key=lambda room_id: (abs(room_id - preferred), room_id)
                )
        return answer


if __name__ == "__main__":
    assert Solution().closestRoom(
        [[2, 2], [1, 2], [3, 2]], [[3, 1], [3, 3], [5, 2]]
    ) == [3, -1, 3]
