import pytest
from bot import Bot
from integration import Integration


def test_create_bot():
    assert Bot('1', 'bot1', 'channel')


def test_empty_bot_id():
    with pytest.raises(Exception) as e_info:
        assert Bot('', 'bot1', 'channel')


def test_empty_bot_name():
    with pytest.raises(Exception) as e_info:
        assert Bot('1', '', 'channel')


def test_empy_channel():
    with pytest.raises(Exception) as e_info:
        assert Bot('1', 'bo1', '')


def test_bot_init_deactivate():
    bot = Bot('1', 'bot1', 'channel')
    expectedResult = False
    assert bot.is_active() == expectedResult


def test_activate_bot():
    bot = Bot('1', 'bot1', 'channel')
    bot.activate()
    assert bot.is_active()


def test_deactivate_bot():
    bot = Bot('1', 'bot1', 'channel')
    bot.activate()
    bot.deactivate()
    assert bot.is_active() == False


def test_bot_init_none_integration():
    bot = Bot('1', 'bot1', 'channel')
    assert bot.integration == None


def test_add_bot_integration():
    bot = Bot('1', 'bot1', 'channel')
    expected_bot_integration = {'client_id': 'client_id', 'token': 'token'}
    integration = Integration(
        expected_bot_integration['client_id'], expected_bot_integration['token'])
    bot.integration = integration
    assert bot.integration == expected_bot_integration
