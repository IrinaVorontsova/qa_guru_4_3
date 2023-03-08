

def test_one():
    assert 1 < 2, "Test failed"


def test_two(x, y):
    assert x > y, f"{y} больше {x}"


print(test_two(2, 1))
print(test_two(1, 2))