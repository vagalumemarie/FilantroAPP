import json
import os

class DataHandler:
    def read_data(self, file_name='user_data'):
        project_root = os.getcwd()
        json_path = os.path.join(project_root, 'Model', file_name + '.json')

        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data


    def write_data(self, file_name='user_data', data={}):
        project_root = os.getcwd()
        json_path = os.path.join(project_root, 'Model', file_name + '.json')

        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)