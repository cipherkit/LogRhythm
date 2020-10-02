import json


class Parser(object):
    """
    Given a set of JSON objects (in a file is fine), for each unique ID field show the unique IPs associated with it and
    the number of times that IP appeared.  Also, sum the score for that ID.  Make no assumptions about the incoming JSON.
    Example input:
    {"id":"test","score":12,"ip":"1.2.3.4","message":"Hi"}
    {"id":"test","score":5,"ip":"1.2.3.5"}
    {"id":"test","score":17,"ip":"1.2.3.4"}
    {"id":"test2","score":9,"ip":"1.2.3.4"}
    Example output:
    test:
        1.2.3.5: 1
        1.2.3.4: 2
        score: 34
    test2:
        1.2.3.4: 1
        score: 9
    Goal: Design and implement both the program to accomplish this, and the script to test the program.  Any language you
    want to use is fine.  Send back the source code for each, along with any assumptions you made.
    """

    def __init__(self, file_data="{}"):
        self.object_list = []
        self.json_data = file_data
        self.store = {}

    def data_in(self, data):
        try:
            json_object = json.loads(data)
            self.add_to_output(json_object)
            return 201, "Object created!"
        except ValueError:
            print(f"Value Error for: {data}")


    def update(self):
        pass

    def clear(self):
        self.object_list = []
        
    def add_to_output(self, json_object):
        self.object_list.append(json_object)

    def merge_identifiers(self, obj_list):
        id_dictionary = {}

        for obj in obj_list:
            score = 0
            if obj['id'] not in id_dictionary.keys():
                id_dictionary[obj['id']] = dict(ips=[obj['ip']], score=obj['score'])
            else:
                id_dictionary[obj['id']]['ips'].append(obj['ip'])
                id_dictionary[obj['id']]['score'] = id_dictionary[obj['id']]['score'] + obj['score']

        for obj_id in id_dictionary:
            id_dictionary[obj_id]['ips'] = self.merge_ip_addresses(id_dictionary[obj_id]['ips'])
        return id_dictionary

    @staticmethod
    def merge_ip_addresses(obj_list):
        ip_dictionary = {}
        for address in obj_list:
            if address not in ip_dictionary.keys():
                ip_dictionary[address] = 1
            else:
                ip_dictionary[address] = ip_dictionary[address] + 1
        return ip_dictionary

    def __str__(self):
        results = self.merge_identifiers(self.object_list)
        string_out = ""
        for key, value in results.items():
            string_out = string_out + f"{key}\n{value['ips']}\nscore: {value['score']}\n"
        return string_out


if __name__ == "__main__":
    # input_file = "example.json.txt"
    parse = Parser()
    parse.data_in('{"id": "test", "score": 12, "ip": "1.2.3.4", "message": "Hi"}')
    parse.data_in('{"id": "test", "score": 5, "ip": "1.2.3.5"}')
    parse.data_in('{"id": "test", "score": 17, "ip": "1.2.3.4"}')
    parse.data_in('{"id": "test2", "score": 9, "ip": "1.2.3.4"}')
    print(parse)
    parse.clear()
    parse.data_in('{"id": "test", "score": 5, "ip": "1.2.3.5"}')
    parse.data_in('{"id": "test", "score": 17, "ip": "1.2.3.4"}')
    parse.data_in('{"id": "test3", "score": 12, "ip": "1.2.3.4", "message": "Hi"}')
    parse.data_in('{"id": "test", "score": 5, "ip": "1.2.3.5"}')
    parse.data_in('{"id": "test", "score": 17, "ip": "1.2.3.4"}')
    parse.data_in('{"id": "test2", "score": 9, "ip": "1.2.3.4"}')
    print(parse)