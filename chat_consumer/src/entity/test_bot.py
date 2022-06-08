import pytest
from bot import Bot


def test_create_bot():
    assert Bot('1', 'bo1', 'channel')


def test_raise_an_exception():
    with pytest.raises(Exception) as e_info:
        assert Bot('', 'bo1', 'channel')


def test_raise_an_exception():
    with pytest.raises(Exception) as e_info:
        assert Bot('1', '', 'channel')


def test_raise_an_exception():
    with pytest.raises(Exception) as e_info:
        assert Bot('1', 'bo1', '')
