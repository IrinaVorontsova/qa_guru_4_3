

def test_one():
    assert 1 < 2, "Test failed"


def test_two(x, y):
    assert x > y, f"{y} больше {x}"

def test_three(z):
    assert z == 0, f"{z} не равно 0"


print(test_two(3, 1))
print(test_two(1, 2))