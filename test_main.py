import pytest
import os
from main import get_top10_words, save_results, read_file


@pytest.fixture
def text():
    return "apple cherry apple cat dog banana apple cherry"

@pytest.mark.parametrize("text, expected_first", [
    ("hello hello world", ("hello", 2)),
    ("cherry apple banana cherry", ("cherry", 2)),
    ("cat DOG cat dog cat", ("cat", 3))
])

def test_get_top10_words(text, expected_first):
    result = get_top10_words(text)
    assert result[0] == expected_first

def test_top_count(text):
    result = get_top10_words(text, top_n=2)
    assert len(result) == 2
    assert result[0] == ("apple", 3)

def test_read_file(tmp_path):
    d = tmp_path / "data"
    d.mkdir()
    file = d / "test.txt"
    content = "hello world"
    file.write_text(content, encoding='utf-8')
    assert read_file(str(file)) == content