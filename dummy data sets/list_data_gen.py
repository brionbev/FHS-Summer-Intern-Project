import random
from venv import create
import data_generator as dg
import json

def gen_data(size:int, size_list, min_date:str, max_date:str):
    '''
    generates dummy data sets for mri, dnp, dcdt, and anon dvoice
    '''
    return_dict = {}
    for i in range(size):
        cohort = dg.generate_cohort()
        dummy = dg.generate_id()

        temp_list = []
        num_dicts = random.randint(1, size_list)
        for j in range((num_dicts)):
            date = dg.generate_dates(min_date, max_date)
            dict_append = {'cohort':cohort, 'date':date, 'dummy_id':dummy}
            temp_list.append(dict_append)
        temp_list = sorted(temp_list, key=lambda d:d['date'])
        
        return_dict[dummy] = temp_list

    return return_dict

def create_json(data_sets:dict, size:int):
    '''
    create the json files containing the dummy data sets
    '''
    for key in data_sets.items():
        params = key[1]
        data = gen_data(size, params[0], params[1], params[2])
        file_name = key[0] + '.json'

        with open(file_name, 'w') as f:
            json.dump(data, f, sort_keys=True, indent=4)
        f.close()

source = {'anon_dvoice':[4, '20050101', '20160630'], 'dcdt':[3, '20210101', '20220101'], 
'dnp':[2, '20210101', '20220101'], 'mri':[4, '20200101', '20211231']}
create_json(source, 40)