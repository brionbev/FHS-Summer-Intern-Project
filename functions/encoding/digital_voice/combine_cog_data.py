import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from pathlib import Path
from fhs_utility.read_pkg.read import read_dictionary_file
from fhs_utility.dementia_review import add_cog_data
from fhs_utility.dementia_review_defaults import add_cog_data_default
import fhs_utility.elastic.id_generator as util
from fhs_utility.save_and_log import save_log
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# M:\mtao\functions\encoding\digital_voicesummer_data_team\data
#data_path = str(Path('.').absolute()).split('summer_data_team',maxsplit=1)[0] + 'summer_data_team\\data'
#data_path = os.path.abspath(os.path.join("..\\functions" , "\\data"))
#dvoice_path = data_path + '\\dvoice.json'

_FRONT_EXT = os.path.splitext(os.path.basename(__file__))[0]
_SAVE_LOG_KW = {'front_ext': _FRONT_EXT, 'ignore_result_keys': {'_save_loc'}}
kwargs = add_cog_data_default()

# data_path = str(Path('.').absolute()).split('summer_data_team',maxsplit=1)[0] + 'summer_data_team\\data'
# data_path = os.path.join('M:' + '\\data') <- What I did before, but does not work on all machines

parent = os.getcwd()
curr_dir = os.path.dirname(os.getcwd())
while (parent != curr_dir):
    parent = os.path.dirname(parent)
    curr_dir = os.path.dirname(curr_dir)

for (root, dirs, files) in os.walk(parent):
    if root.split('\\')[-1] == 'data':
        parent = root
        break
dvoice_path = os.path.abspath(os.path.join(parent, 'dvoice.json'))



#data_path = str(Path('.').absolute()).split('summer_data_team',maxsplit=1)[0] + 'summer_data_team\\data'
data_path = Path('.').absolute().parent.parent.parent.parent

# dvoice_path = os.path.join(data_path,'dvoice.json')
dvoice_path = os.path.join(data_path, 'bbrion', 'data','dvoice_dummy.json')

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

    id_list = util.query_ids(client,'student-dvoice')
    #id_list = [key for key in data_json(dvoice_path)] # for testing when json can't be loaded from the cloud

    dummy_list = [None] * len(id_list)
    for idx,value in enumerate(id_list):
        dummy_list[idx] = value.split('-')[0]

    ###Create list of streams of indices

    streams = [util.get_id(id_list,i,auth) for i in test_paths]


    sets = [set() for i in range(len(test_paths))]
    for i,stream in enumerate(streams):
        for value in stream:
            sets[i].add(value['_id'].split('-')[0])


    dvoice_json = data_json(dvoice_path)
    result = {}
    for i in dummy_list:
        resp = dvoice_json[i]
        #print(resp)
        for idx, j in enumerate(sets):
            if i in j:
                resp[test_paths[idx]] = 1
            else:
                resp[test_paths[idx]] = 0

        
        result[i] = resp
        print(result[i])
    return {'final':result}
(encode(['dvoice']))
