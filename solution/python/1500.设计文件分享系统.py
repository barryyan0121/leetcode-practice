import heapq


class FileSharing:
    def __init__(self, m: int):
        self.chunks = [set() for _ in range(m + 1)]
        self.users = {}
        self.available = []
        self.next_id = 1

    def join(self, ownedChunks: list[int]) -> int:
        if self.available:
            user_id = heapq.heappop(self.available)
        else:
            user_id = self.next_id
            self.next_id += 1
        self.users[user_id] = set(ownedChunks)
        for chunk in ownedChunks:
            self.chunks[chunk].add(user_id)
        return user_id

    def leave(self, userID: int) -> None:
        for chunk in self.users.pop(userID):
            self.chunks[chunk].remove(userID)
        heapq.heappush(self.available, userID)

    def request(self, userID: int, chunkID: int) -> list[int]:
        owners = sorted(self.chunks[chunkID])
        if owners:
            self.users[userID].add(chunkID)
            self.chunks[chunkID].add(userID)
        return owners


if __name__ == "__main__":
    test_cases = [
        (
            4,
            [([1, 2], 1), ([2, 3], 2), ([4], 3), ([], 1)],
        )
    ]
    for _, (m, joins) in enumerate(test_cases):
        system = FileSharing(m)
        first, second, third = [system.join(chunks) for chunks, _ in joins[:3]]
        assert [first, second, third] == [1, 2, 3]
        assert system.request(first, 3) == [2]
        assert system.request(second, 2) == [1, 2]
        system.leave(first)
        assert system.request(second, 1) == []
        system.leave(second)
        assert system.join(joins[3][0]) == joins[3][1]
