from venv import create
import data_generator as dg
import json

def gen_data(size:int, data_type:str):
    '''
    generates dummy data sets for apoe, dementia review, dvoice, education,
    and neuropath
    '''
    data_type = data_type.lower()
    
    return_dict = {}
    for i in range(size):
        methods = {'edu':dg.generate_edu_data(), 'apoe':dg.generate_apoe(), 'dvoice':
        dg.generate_dvoice_data()}

        dummy = dg.generate_id()
        cohort = dg.generate_cohort()

        dict_append = {'cohort':cohort, 'dummy_id':dummy}
        if data_type in methods:
            func = methods[data_type]
            dict_append[func[-1]] = func[0]

        return_dict[dummy] = dict_append

    return return_dict


def create_json(data_sets:list, size:int):
    '''
    create the json files containing the dummy data sets
    '''
    for item in data_sets:
        data = gen_data(size, item)
        file_name = item + '.json'

        with open(file_name, 'w') as f:
            json.dump(data, f, sort_keys=True, indent=4)
        f.close()

source =['apoe', 'dr', 'dvoice', 'edu', 'np']
create_json(source, 40)
