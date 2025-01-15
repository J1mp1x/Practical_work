from typing import Any


# Write the function that checks whether the element `val`
# is present in the list `l`.
# Return `True` if present and `False` otherwise
def contains(l: list[Any], val: Any) -> bool:
    pass


# Do not change the below's code
if __name__ == "__main__":
    l = [3, 6, 1, 2]

    assert contains(l, 1) == True
    assert contains(l, -1) == False
    assert contains(l, 2) == True
    assert contains(l, "c") == False
    assert contains(["a", "c", "c"], "c") == True
