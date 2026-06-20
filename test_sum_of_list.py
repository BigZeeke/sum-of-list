from sum_list import sum_of_lists


def run_tests(sum_of_lists):
    assert sum_of_lists([3, 5, 8, 2]) == 18
    assert sum_of_lists([0]) == 0
    assert sum_of_lists([0, ]) == 0

    try:
        sum_of_lists([2, "two", 3])
        raise AssertionError(
            "Test failed: expected TypeError but none was raised")
    except TypeError:
        pass


print("All tests passed")
