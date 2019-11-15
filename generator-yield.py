def test():
    for i in range(4):
        yield

print(next(test()))
