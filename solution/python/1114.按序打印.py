from threading import Semaphore, Thread


class Foo:
    def __init__(self):
        self.second_turn = Semaphore(0)
        self.third_turn = Semaphore(0)

    def first(self, printFirst) -> None:
        printFirst()
        self.second_turn.release()

    def second(self, printSecond) -> None:
        self.second_turn.acquire()
        printSecond()
        self.third_turn.release()

    def third(self, printThird) -> None:
        self.third_turn.acquire()
        printThird()


if __name__ == "__main__":
    test_cases = ["firstsecondthird"]
    for _, expected in enumerate(test_cases):
        output = []
        foo = Foo()
        threads = [
            Thread(target=foo.third, args=(lambda: output.append("third"),)),
            Thread(target=foo.second, args=(lambda: output.append("second"),)),
            Thread(target=foo.first, args=(lambda: output.append("first"),)),
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        assert "".join(output) == expected
