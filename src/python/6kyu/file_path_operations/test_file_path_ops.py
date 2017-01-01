import pytest
"""
TEST CASES:

master = FileMaster('/Users/person1/Pictures/house.png')
test.describe('Description Test Cases')
test.assert_equals(master.extension(), 'png')
test.assert_equals(master.filename(), 'house')
test.assert_equals(master.dirpath(), '/Users/person1/Pictures/')
"""


@pytest.fixture
def file_master():
    from file_path_ops import FileMaster
    return FileMaster('/Users/person1/Pictures/house.png')


def test_FileMaster_extension(file_master):
    assert file_master.extension() == 'png'


def test_FileMaster_filename(file_master):
    assert file_master.filename() == 'house'


def test_FileMaster(file_master):
    assert file_master.dirpath() == '/Users/person1/Pictures/'
