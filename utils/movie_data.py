import pytest

from test_data.test_data import TestData


@pytest.fixture(params=TestData.movie_name)
def get_movie_name(request):
    return request.param
