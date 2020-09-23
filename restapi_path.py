import json
import sys

class OpenAPI:

    def __init__(self, fp):
        self.fp = fp
        self.json_load()

    def json_load(self):
        with open(self.fp, 'r') as file:
            self.paths = json.load(file)

    def paths_with(self, keyword):
        path_list = []
        if keyword != '':
            for path in self.paths['paths'].keys():
                if keyword in path:
                    path_list.append(path)

        return path_list

    def get_paths(self):
        path_list = []
        for path in self.paths['paths'].keys():
            path_list.append(path)
        
        return path_list


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Assume its a filename
        filename = sys.argv[1]
        myswag = OpenAPI(filename)

        while True:
            keyword = input('Enter keyword: ')
            if keyword == 'quit':
                break
            
            paths = myswag.paths_with(keyword)
            for path in paths:
                print(path)
    else:
        print('Usage: restapi_path.py path/filename')

        

