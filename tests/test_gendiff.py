import pytest
from gendiff.comparison import generate_diff


@pytest.mark.parametrize(
    'file1,file2,form,expected',
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', "stylish", 'tests/fixtures/test_stylish1'),
        ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', "stylish", 'tests/fixtures/test_stylish1'),
        ('tests/fixtures/file1.json', 'tests/fixtures/file1.yml', "stylish", 'tests/fixtures/test_stylish2'),
        ('tests/fixtures/file2.json', 'tests/fixtures/file2.yml', "stylish", 'tests/fixtures/test_stylish3'),
        ('tests/fixtures/file4.json', 'tests/fixtures/file4.yml', "stylish", 'tests/fixtures/nested3'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "plain", 'tests/fixtures/format_plain'),
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.yml', "json", 'tests/fixtures/format_json')],
)
def test_generate_diff(file1, file2, form, expected):
    assert generate_diff(file1, file2, form) == open(expected).read().rstrip()
