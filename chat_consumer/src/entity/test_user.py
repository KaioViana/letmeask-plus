import pytest
from user import User

def test_create_user():
    assert User('1', 'user name', 'nickname', 'channel')

def test_empty_user_id():
    with pytest.raises(Exception):
        assert User('', 'user name', 'nickname', 'channel')

def test_empty_name():
    with pytest.raises(Exception):
        assert User('1', '', 'nickname', 'channel')

def test_empty_nickname():
    with pytest.raises(Exception):
        assert User('1', 'name', '', 'channel')

def test_empty_user_channel():
    with pytest.raises(Exception):
        assert User('1', 'name', 'nickname', '')

def test_change_nickname():
    expected_name = 'nickname2'
    user = User('1', 'name', 'nickname', 'channel')
    user.change_nickname(expected_name)
    assert user.get_nickname() == expected_name

def test_change_user_channel():
    expected_user_channel = 'channel2'
    user = User('1', 'name', 'nickname', 'channel')
    user.change_user_channel(expected_user_channel)
    assert user.get_user_channel() == expected_user_channel
