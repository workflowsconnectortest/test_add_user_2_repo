""" TEST """
import pytest


@pytest.mark.test
def test_open_browser(driver_session):
    """
    TEST
    :param driver_session:
    :return:
    """
    pass


@pytest.mark.test
def test_open_apple(driver_session):
    """
    TEST
    :param driver_session:
    :return:
    """
    driver_session.get("https://www.apple.com")
