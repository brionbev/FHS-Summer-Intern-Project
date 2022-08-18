import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from fhs_utility.read_pkg.read import read_dictionary_file
from fhs_utility.dementia_review import add_cog_data
from fhs_utility.dementia_review_defaults import add_cog_data_default
import fhs_utility.elastic.id_generator as util
from pathlib import Path
from fhs_utility.save_and_log import save_log

_FRONT_EXT = os.path.splitext(os.path.basename(__file__))[0]
_SAVE_LOG_KW = {'front_ext': _FRONT_EXT, 'ignore_result_keys': {'_save_loc'}}
kwargs = add_cog_data_default()

parent = os.getcwd()
curr_dir = os.path.dirname(os.getcwd())
while (parent != curr_dir):
    parent = os.path.dirname(parent)
    curr_dir = os.path.dirname(curr_dir)

for (root, dirs, files) in os.walk(parent):
    if root.split('\\')[-1] == 'data':
        parent = root
        break
dcdt_path = os.path.abspath(os.path.join(parent, 'dcdt.json'))

def data_json(some_path):
    '''Returns a dataset json'''
    return read_dictionary_file(some_path)

def encode(tests:list):
    '''Returns a generator of tuples'''
    test_paths = []
    for i in tests:
        path = 'student-' + i
        test_paths.append(path)

    auth = ('student','fhs1234')
    util.make_client(auth, None)
    client = util.get_client()

    id_list = util.query_ids(client,'student-dcdt')
    # id_list = [key for key in data_json(dcdt_path)] # for testing when json can't be loaded from the cloud

    dummy_list = [None] * len(id_list)
    for idx,value in enumerate(id_list):
        dummy_list[idx] = value.split('-')[0]

    ###Create list of streams of indices

    streams = [util.get_id(id_list,i,auth) for i in test_paths] 


    sets = [set() for i in range(len(test_paths))]
    for i,stream in enumerate(streams):
        for value in stream:
            sets[i].add(value['_id'].split('-')[0])


    dcdt_json = data_json(dcdt_path)
    result = {}
    for i in dummy_list:
        resp = dcdt_json[i]
       # print(resp)

        # loop through every dictionary inside the list
        for idx, j in enumerate(sets): # idx is always 0, j is a set of all the ids in the json file
            not_found = True
            for dict in resp:
                if (test_paths[idx] not in dict or dict[test_paths[idx]] == 0) and (i in j and not_found):
                    dict[test_paths[idx]] = 1
                    not_found = False
                elif (test_paths[idx] not in dict):
                    dict[test_paths[idx]] = 0
                    
        result[i] = resp
        print(result[i])
    return {'final':result}

encode(['dcdt'])


    
