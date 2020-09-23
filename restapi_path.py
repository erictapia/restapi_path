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
    #myswag = OpenAPI('openapi/dnac/Release-1310-swagger.Build1220.annotated.json')
    myswag = OpenAPI('openapi/meraki/v0.json')
    myswag = OpenAPI('openapi/sd-wan/nms-administration.json')
    # paths = myswag.get_paths()
    # for path in paths:
    #     print(path)
    
    while True:
        keyword = input('Enter keyword: ')
        if keyword == 'quit':
            break
        
        paths = myswag.paths_with(keyword)
        for path in paths:
            print(path)

        

