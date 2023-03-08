

def test_one(x):
    assert x!= 0


def test_two(x, y):
    assert x > y, f"{y} больше {x}"


print(test_two(2, 1))
print(test_two(1, 2))

print(test_one(1))