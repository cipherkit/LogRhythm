import json
import logging as log

log.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=log.DEBUG)


class Parser(object):
    """
        This is a script to simply get the job of parsing input done. It's a top down approach for a
        Non-recursive descent parser. This approach was chosen for it's simplicity to implement.

        Usage:
        instance = Parser()
        instance.data_in(data) where data is a valid JSON string
        print(instance)
        instance.clear()
        ... Do something else with it ...
    """

    def __init__(self, file_data="{}"):
        self.object_list = []
        self.json_data = file_data
        log.debug("New Parser instance created")

    def data_in(self, data):
        try:
            json_object = json.loads(data)
            self.add_to_output(json_object)
            log.debug(f"New json input added {data}")
            return 201, "Object created!"
        except ValueError:
            log.error(f"Value Error for: {data}")

    def update(self):
        pass

    def clear(self):
        self.object_list = []
        log.debug("Input cleared.")
        
    def add_to_output(self, json_object):
        self.object_list.append(json_object)

    def merge_identifiers(self, obj_list):
        id_dictionary = {}
        for obj in obj_list:
            if obj['id'] not in id_dictionary.keys():
                id_dictionary[obj['id']] = dict(ips=[obj['ip']], score=obj['score'])
            else:
                id_dictionary[obj['id']]['ips'].append(obj['ip'])
                id_dictionary[obj['id']]['score'] = id_dictionary[obj['id']]['score'] + obj['score']
        for obj_id in id_dictionary:
            id_dictionary[obj_id]['ips'] = self.merge_ip_addresses(id_dictionary[obj_id]['ips'])
        log.debug("input merged into a solution.")
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

    def __repr__(self):
        return str(self.merge_identifiers(self.object_list))

    def __str__(self):
        results = self.merge_identifiers(self.object_list)
        string_out = ""
        for key, value in results.items():
            string_out = string_out + f"{key}\n{value['ips']}\nscore: {value['score']}\n"
        return string_out

    def file_input(self, file_data):
        for line in file_data:
            obj = json.loads(str(line))
            self.object_list.append(obj)
        log.debug("File data loaded.")


if __name__ == "__main__":
    # example 1
    parse = Parser()
    parse.data_in('{"id": "test", "score": 12, "ip": "1.2.3.4", "message": "Hi"}')
    parse.data_in('{"id": "test", "score": 5, "ip": "1.2.3.5"}')
    parse.data_in('{"id": "test", "score": 17, "ip": "1.2.3.4"}')
    parse.data_in('{"id": "test2", "score": 9, "ip": "1.2.3.4"}')
    print(parse)
    parse.clear()

    # example 2
    parse.data_in('{"id": "test", "score": 5, "ip": "1.2.3.5"}')
    parse.data_in('{"id": "test", "score": 17, "ip": "1.2.3.4"}')
    parse.data_in('{"id": "test3", "score": 12, "ip": "1.2.3.4", "message": "Hi"}')
    parse.data_in('{"id": "test", "score": 5, "ip": "1.2.3.5"}')
    parse.data_in('{"id": "test", "score": 17, "ip": "1.2.3.4"}')
    parse.data_in('{"id": "test2", "score": 9, "ip": "1.2.3.4"}')
    print(parse)
    print(repr(parse))
    print(parse.object_list)
    parse.clear()

    # example 3
    with open("./example.json.txt") as f:
        parse.file_input(f)
        print(parse)
