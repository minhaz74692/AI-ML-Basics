class RemoteControl:
    def __init__(self):
        self.channels = ["cnn", "abc", "espn", "gtv"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        print("Next Channel,", self.channels[self.index])
        return self.channels[self.index]

if __name__ == "__main__":
    rc = RemoteControl()
    itr = iter(rc)
    # rc.__next__()
    # print(next(itr))
    # print(next(itr))
    # print(next(itr))
    # print(next(itr))
    # print(next(itr))
    # print(next(itr))