import os

from pathlib import Path

from fhs_utility.read_pkg.read import read_dictionary_file
from fhs_utility.dementia_review import add_cog_data
from fhs_utility.dementia_review_defaults import add_cog_data_default
import fhs_utility.elastic.id_generator as util

from pathlib import Path

from fhs_utility.save_and_log import save_log
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



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
pib_path = os.path.abspath(os.path.join(parent, 'pib.json'))


def data_json(some_path):
    '''Returns a dataset json'''
    return read_dictionary_file(some_path)



def encode(tests:list):
    '''Returns a generator of tuples'''
    test_paths = []
    for i in tests:
        path = 'student-' + i
        test_paths.append(path)


#creates authentication for access to eletricsearch


    auth = ('student','fhs1234')
    util.make_client(auth, None)
    client = util.get_client()

    id_list = util.query_ids(client,'student-pib')
    dummy_list = [None] * len(id_list)
    for idx,value in enumerate(id_list):
        dummy_list[idx] = value.split('-')[0]

    ###Create list of streams of indices


    streams = [util.get_id(id_list,i,auth) for i in test_paths] 

    sets = [set() for i in range(len(test_paths))]
    for i,stream in enumerate(streams):
        for value in stream:
            sets[i].add(value['_id'].split('-')[0])



#creates an object that sets path for the json file and results in
#giving the data for respective json file


    pib_json = data_json(pib_path)
    result = {}
    for i in dummy_list:
        resp = pib_json[i]

        for idx, j in enumerate(sets):
            if i in j:
                resp[test_paths[idx]] = 1
            else:
                resp[test_paths[idx]] = 0


        result[i] = resp
        print(resp)
    return {'final':result}
(encode(['pib']))

#final return & print statements
