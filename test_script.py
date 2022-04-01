import unittest
from unittest.mock import patch
from io import StringIO
from script import (
    data_input,
    data_handling,
    output_packaging,
    validation,
)

# def mocked_requests_get(*args, **kwargs):
#     class MockResponse:
#         def __init__(self, json_data, status_code):
#             self.json_data = json_data
#             self.status_code = status_code

#         def json(self):
#             return self.json_data

#     if args[0] == 'http://someurl.com/test.json':
#         return MockResponse({"key1": "value1"}, 200)
#     elif args[0] == 'http://someotherurl.com/anothertest.json':
#         return MockResponse({"key2": "value2"}, 200)

#     return MockResponse(None, 404)


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
        
    if args[0] == "http://www.bbc.co.uk/iplayer":
        return MockResponse({}, 200)


class internal_test(unittest.TestCase):

    @patch('sys.stdin', StringIO("http://www.bbc.co.uk/iplayer\nhttp://www.bbc.co.uk/iplayer\n"))    
    def test_standard_input(self):
        # Check input and output match
        expected_out = ['http://www.bbc.co.uk/iplayer',
                        'http://www.bbc.co.uk/iplayer']
        self.assertEqual(data_input(), expected_out)

    def test_list_input(self):
        newline_list = "http://www.bbc.co.uk/iplayer\nhttp://www.bbc.co.uk/iplayer\n"
        expected_out = ['http://www.bbc.co.uk/iplayer',
                        'http://www.bbc.co.uk/iplayer']
        self.assertEqual(data_handling(newline_list), expected_out)

    def test_json_packaging(self):
        class testResponse:
            url = "https://www.bbc.co.uk/iplayer"
            status_code = 200,
            content = "This is just a test"

        expected_out = '{"Url": "https://www.bbc.co.uk/iplayer", "Status-code": [200], "Content-length": 19}'
        self.assertEqual(output_packaging(testResponse), expected_out)
        
    @patch("requests.get", side_effect=mocked_requests_get)
    def test_response(self, mock_get):
        url = "Abc"
        expected_out = True
        self.assertEqual(validation(url), expected_out)

if __name__ == "__main__":
    unittest.main()
