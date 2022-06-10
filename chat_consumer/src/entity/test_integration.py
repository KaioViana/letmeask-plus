import pytest
from integration import Integration


def test_create_integration():
    assert Integration('client_id', 'token')


def test_empty_client_id():
    with pytest.raises(Exception) as e_info:
        assert Integration('', 'token')


def test_empty_token():
    with pytest.raises(Exception) as e_info:
        assert Integration('client_id', '')


def test_change_integration():
    expected_values = {'client_id': 'expected_client_id',
                       'token': 'expected_token'}
    integration = Integration('client_id', 'token')
    integration2 = integration.change_integration(
        expected_values['client_id'], expected_values['token'])
    assert integration2.get_integration_values() == expected_values


def test_change_integration_client_id_to_existing_client_id():
    integration = Integration('client_id', 'token')
    with pytest.raises(Exception) as e_info:
        assert integration.change_integration('client_id', 'new_token')


def test_change_integration_token_to_existing_token():
    integration = Integration('client_id', 'token')
    with pytest.raises(Exception) as e_info:
        assert integration.change_integration('new_client_id', 'token')
