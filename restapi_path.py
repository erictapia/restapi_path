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
                if keyword.lower() in path.lower():
                    path_list.append(path)

        return path_list

    def get_paths(self):
        path_list = []
        for path in self.paths['paths'].keys():
            path_list.append(path)
        
        return path_list


if __name__ == '__main__':
    # TODO
    # ========================
    # {verb} keyword {index}
    # {verb} path?
    # {verb} path*

    if len(sys.argv) > 1:
        # Assume its a filename
        filename = sys.argv[1]
        myswag = OpenAPI(filename)

        print('Rest API Path')
        print('Enter a keyword when you are done enter "quit"')

        while True:
            keyword = input() #input('Enter keyword: ')
            if keyword == 'quit':
                break
            
            if keyword == '':
                continue

            paths = myswag.paths_with(keyword)

            if len(paths) == 0:
                print('No results')
                print()

            for (i,path) in enumerate(paths):
                print(f'{i}: {path}')
    else:
        print('Usage: restapi_path.py path/filename')