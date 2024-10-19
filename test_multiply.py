from multiply import multiply

def test_multiply_one_by_one():
    assert multiply(1, 1) == 1

def test_multiply_two_by_two():
    assert multiply(2, 2) == 4

def test_multiply_three_by_three():
    assert multiply(3, 3) == 9

def test_multiply_four_by_four():
    assert multiply(4, 4) == 16

def test_multiply_large_numbers():
    assert multiply(23, 45) == 23 * 45
