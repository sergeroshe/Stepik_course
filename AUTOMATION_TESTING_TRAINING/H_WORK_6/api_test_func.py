import sys

import requests

from datetime import datetime

ENDPOINT = 'https://cat-fact.herokuapp.com/facts'


class Tests:

    @staticmethod
    def is_request_ok_test():
        response = requests.get(ENDPOINT)
        assert response.ok

    @staticmethod
    def is_response_non_empty_test():
        response = requests.get(ENDPOINT)
        assert response.json()

    @staticmethod
    def is_created_in_21_century_test():
        response = requests.get(ENDPOINT)
        facts_data = response.json()

        assert datetime.strptime(facts_data[0]['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ") > \
               datetime.strptime('2000-01-01T00:00:00.000Z', "%Y-%m-%dT%H:%M:%S.%fZ")

    # @staticmethod
    # def is_text_non_empty():
    #     response = requests.get(ENDPOINT)
    #     facts_data = response.json()
    #     assert isinstance(facts_data, list)
    #     assert all(fact['text'] for fact in facts_data)

    # TODO: createdAt after 2000-01-01T00:00:00.000Z
    #  use c datetime.strftime
    # @staticmethod


if __name__ == '__main__':
    # TODO if agr(s) has been sent - execute only marked tests
    # TODO if no args -> execute all
    all_test_names = [attr for attr in dir(Tests) if attr.endswith('_test')]
    test_names = sys.argv[1:] if len(sys.argv) > 1 else all_test_names

    for name in test_names:
        test_method = getattr(Tests, name, None)
        if not test_method:
            print(f'Test method with name=[{name}] not exist')
            continue

        test_method()
        print(f'Test {name} passed.')
