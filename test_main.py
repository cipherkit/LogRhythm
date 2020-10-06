import json
import unittest
from json import JSONDecodeError

from main import Parser


class TestParser(unittest.TestCase):

    def setUp(self):
        self.parse = Parser()

    def test_input_file(self):
        file_text = "./example.json.txt"
        with open(file_text) as f:
            self.parse.file_input(f)
            expected = '[{"id":"test","score":12,"ip":"1.2.3.4","message":"Hi"},' \
                       '{"id":"test","score":5,"ip":"1.2.3.5"},' \
                       '{"id":"test","score":17,"ip":"1.2.3.4"},' \
                       '{"id":"test2","score":9,"ip":"1.2.3.4"}]'
            json_expectation = json.loads(expected)
            self.assertEqual(json_expectation, self.parse.object_list)

    def test_data_in(self):
        string_input = '{"test": "id"}'

        result = self.parse.data_in(string_input)
        self.assertEqual(201, result[0])

    def test_data_in_not_json(self):
        not_json = "[}"
        result = self.parse.data_in(not_json)
        # self.assertRaises(JSONDecodeError, "ValueError not raised.")
        self.assertRaises(ValueError)

    def test_result_out(self):
        self.parse.data_in('{"id":"test","score":12,"ip":"1.2.3.4","message":"Hi"}')
        self.parse.data_in('{"id":"test","score":5,"ip":"1.2.3.5"}')
        expected = "test\n{'1.2.3.4': 1, '1.2.3.5': 1}\nscore: 17\n"
        self.assertEqual(expected, str(self.parse))

    def test_merge_identifiers(self):
        obj_list = [dict(id="test", score=12, ip="1.2.3.4", message="Hi"),
                    dict(id="test", score=12, ip="1.2.3.4", message="Hi"),
                    dict(id="test2", score=24, ip="1.2.3.5")]
        results = self.parse.merge_identifiers(obj_list)
        expected = {'test': {'ips': {'1.2.3.4': 2}, 'score': 24},
                    'test2': {'ips': {'1.2.3.5': 1}, 'score': 24}}
        self.assertEqual(expected, results, "Merge identifiers not equal did something change?")

    def test_merge_ip_addresses(self):
        obj_dictionary = ['1.2.3.4', '1.2.3.5']
        results = self.parse.merge_ip_addresses(obj_dictionary)
        expected = {'1.2.3.4': 1, '1.2.3.5': 1}
        self.assertEqual(expected, results)

    def add_to_output(self):
        json_test = dict(id="test", score=12, ip="1.2.3.4", message="Hi")
        parse = Parser()
        parse.add_to_output(json_test)
        self.assertEqual(parse.object_list[-1], json_test)

    def tearDown(self) -> None: ...
