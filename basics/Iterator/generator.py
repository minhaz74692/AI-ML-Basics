def remote_control_generator():
    yield "cnn"
    yield "espn"
    yield "myTV"
    yield "GTV"

if __name__=="__main__":
    itr = remote_control_generator()
    print(itr)
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    for c in remote_control_generator():
        print("Channel: ", c)