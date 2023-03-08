

def test_one(x):
    assert x != 0, f"{x} равен нулю"


def test_two(x, y):
    assert x > y, f"{y} больше {x}"

def test_three(x):
    assert x == 0


print(test_two(2, 1))
print(test_two(1, 2))

print(test_one(1))