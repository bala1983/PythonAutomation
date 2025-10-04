import requests
import pytest
import logging

class TestCarsGetSorting:

    logger = logging.Logger('car log')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @pytest.mark.parametrize('sort_by, limit', [
        ("price", 2),
        ("brand", None),
        (None, 2),
        ("year", 3),
        (None, None)
    ])

    def test_get_cars(self, auth_user, sort_by, limit):
        header = {"Authorization":f"Bearer {auth_user}"}
        parameters = {}
        if sort_by:
            parameters['sort_by'] = sort_by
        if limit:
            parameters['limit'] = limit

        print(bool(sort_by))
        print(bool(limit))

        response = requests.get(f'http://127.0.0.1:8080/cars', headers=header, params=parameters)

        logging.info(response.content)

        print(type(response.json()))

        assert isinstance(response.json(), list)
        if limit:
            assert limit == (len(response.json()))