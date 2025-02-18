def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5  # This should pass
    assert add(1, 1) == 3  # This should fail to show test failure
