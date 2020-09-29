import json
import sys

class OpenAPI:

    def __init__(self, fp):
        self.fp = fp
        self.json_load()

    def json_load(self):
        with open(self.fp, 'r') as file:
            self.paths = json.load(file)

    def paths_with(self, keyword, verb=None, index=None):
        path_list = []

        for path in self.paths['paths'].keys():
            if keyword.lower() in path.lower():
                if verb != None:
                    if verb in self.paths['paths'][path].keys():
                        path_list.append(path)
                
                else:
                    path_list.append(path)

        if index != None:
            path_list = [path_list[index]]

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
        #print(f'\t Base URL: {myswag.get_host()}{myswag.get_base_path()}')
        print()
        print('Enter a keyword using format shown below or "quit" to exit')
        print('\t keyword')
        print('\t verb keyword')
        print('\t verb keyword index')
        print()
        print('Keyword: any word that could be part of the REST API URL path')
        print('Verb: any HTTP request verb')
        print('Index: The index to get more information about one path from the result set.')
        print('='*79)

        while True:
            keyword = input() #input('Enter keyword: ')
            if keyword == 'quit':
                break
            
            if keyword == '':
                continue
            
            # Hack: Remove leading, trailing, and consecutive spaces
            #       Then split
            words = " ".join(keyword.split()).split()
            
            word_count = len(words)
            if word_count == 3:
                verb = words[0]
                keyword = words[1]
                index = int(words[2])
                paths = myswag.paths_with(keyword, verb, index)

            elif word_count == 2:
                verb = words[0]
                keyword = words[1]
                paths = myswag.paths_with(keyword, verb)

            else:
                paths = myswag.paths_with(keyword)

            if len(paths) == 0:
                print('No results')
                
            elif len(paths) == 1:
                print(f'{paths[0]}')
            
            else:
                for (i,path) in enumerate(paths):
                    print(f'{i}: {path}')

            print()
    else:
        print('Usage: restapi_path.py path/filename')