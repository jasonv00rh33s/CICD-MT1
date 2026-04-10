import pytest
import main

@pytest.fixture
def text():
    return "apple cherry apple cat dog banana apple cherry"

@pytest.mark.parametrize("text, expected_first", [
    ("hello hello world", ("hello", 2)),
    ("cherry apple banana cherry", ("cherry", 2)),
    ("cat DOG cat dog cat", ("cat", 3))
])
