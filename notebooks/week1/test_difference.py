def difference(x, y):
    return abs(x - y)

def test_difference():
    assert difference(2, 1) == 1
    assert difference(1, 2) == 1