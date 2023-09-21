import sys
from datetime import datetime

import requests

ENDPOINT = 'https://cat-fact.herokuapp.com/facts'


class ApiTest:
    @staticmethod
    def get_response(self):
        return requests.get(ENDPOINT)

    @staticmethod
    def get_data(self):
        response = ApiTest.get_response(self)
        return response.json()

    @staticmethod
    def is_created_after(self):
        response = ApiTest.get_response(self)
        return response.json()

    def run(self) -> bool:
        raise NotImplementedError


class Tests:
    class TestIsRequestOk(ApiTest):
        def run(self):
            response = self.get_response(self)
            assert response.ok

    class TestIsResponseNonEmpty(ApiTest):
        def run(self):
            assert self.get_data(self)

    class TestTextNonEmpty(ApiTest):
        def run(self):
            facts_data = self.get_data(self)
            assert isinstance(facts_data, list)
            assert all(fact['text'] for fact in facts_data)

    class TestIsCreatedAfter(ApiTest):
        def run(self):
            response = requests.get(ENDPOINT)
            facts_data = response.json()

            assert datetime.strptime(facts_data[0]['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ") > \
                   datetime.strptime('2000-01-01T00:00:00.000Z', "%Y-%m-%dT%H:%M:%S.%fZ")

    # class TestIsNotDeleted(ApiTest):
    #     def run(self):
    #         facts_data = self.get_data(self)
    #         assert isinstance(facts_data, list)
    #         assert all(fact['deleted'] for fact in facts_data)

    # TODO: createdAt after 2000-01-01T00:00:00.000Z use datetime.strptime datetime.strftime


if __name__ == '__main__':
    # TODO if agr(s) has been sent - execute only marked tests
    # TODO if no args -> execute all
    all_test_names = [attr for attr in dir(Tests) if attr.startswith('Test')]
    test_names = sys.argv[1:] if len(sys.argv) > 1 else all_test_names

    for name in test_names:
        test_class = getattr(Tests, name, None)
        if not test_class:
            print(f'Test method with name=[{name}] does not exist')
            continue

        test = test_class()
        test.run()
        print(f'Test {name} passed.')

