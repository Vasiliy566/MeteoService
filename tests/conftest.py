import pytest
from aioresponses import aioresponses

from meteo_service.config import Config


@pytest.fixture
def test_config() -> Config:
    return Config(open_meteo_api="http://test_meteo_api.com")


@pytest.fixture
def mocked():
    with aioresponses() as m:
        yield m
