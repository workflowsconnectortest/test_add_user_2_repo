import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver_session():

    driver_session = webdriver.Chrome()
    yield driver_session
    driver_session.quit()

@pytest.fixture(scope="function")
def data_storage():
    """
    Pass data around
    :return:
    """
    data_storage = {}
    yield data_storage
