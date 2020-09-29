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

    def get_title(self):
        return self.paths['info']['title']

    def get_version(self):
        return self.paths['info']['version']
    
    def get_base_path(self):
        return self.paths['basePath']
    
    def get_host(self):
        return self.paths['host']

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
        title = myswag.get_title()
        version = myswag.get_version()

        print('='*79)
        print('Rest API Path loaded OpenAPI specification:')
        print(f'\t Title: {title}')
        print(f'\t Version: {version}')
        print(f'\t Base URL: {myswag.get_host()}{myswag.get_base_path()}')
        print()
        print('Enter a keyword or "quit" to exit')
        print('='*79)

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