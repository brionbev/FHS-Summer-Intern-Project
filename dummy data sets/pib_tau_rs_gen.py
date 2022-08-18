import data_generator as dg
import json

def gen_data(size:int, data_type:str, min_date:str, max_date:str):
    '''
    generates dummy data sets for pib, tau, and race_sex
    '''
    allowed = ['pib', 'tau', 'rs']
    data_type = data_type.lower()
   
    if data_type not in allowed:
        raise Exception("data_type must be pib, tau, or rs")

    temp_list = []
    for i in range(size):
        cohort = dg.generate_cohort()
        date = dg.generate_dates(min_date, max_date)
        dummy = dg.generate_id()

        dict_append = {}
        if data_type == 'rs':
            rs = dg.generate_race_sex()
            dict_append = {'cohort':cohort, 'dob_str':date, 'dummy_id':dummy, 'race1':rs[0],
            'sex':rs[1]}
        else:
            dict_append = {'cohort':cohort, 'date':date, 'dummy_id':dummy, 
            'scan_type':data_type.upper(), 'scanner_model':dg.generate_scan_mod()}
        temp_list.append(dict_append)

    temp_list = sorted(temp_list, key=lambda d:d['dummy_id'])
    return_dict = {key['dummy_id']:key for key in temp_list}
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

source = {'pib':['pib', '20210101', '20220101'], 'tau':['tau', '20210101', '20220101'], 
'race_sex':['rs', '18900101', '19901231']}
create_json(source, 40)
