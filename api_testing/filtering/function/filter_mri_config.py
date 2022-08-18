'''Config file for mri filtering script'''

from pathlib import Path
import os
from fhs_utility.handle_dates import date_parse as dp

auth = ('student','fhs1234')


def mri(idx_list):
    ids = [val['_source']['dummy_id'] for val in idx_list]

    return {
        'bool':{
            'must':[
                {'terms': {'dummy_id.keyword': ids}}
            ]
        }
    }



def date_query(value):
    '''Passes value into date_query'''
    dummy_id = value['_id'].split('-')[0]
    date = value['_id'].split('-')[1]
    range = '160'
    return {
                'bool' : {
                    'must' : [
                        {'term' : {'dummy_id.keyword' : dummy_id}}
                        
                    ],
                    'filter' : [
                        {'range' : {'date' : {'gte' : date +'||-' + range + 'd','lte' : date +'||+' + range + 'd'}}}
                    ]
                }
                        
            }
 

data_path = str(Path('.').absolute()).split('summer_data_team',maxsplit=1)[0] + 'summer_data_team\\data'
data_path = Path('.').absolute().parent.parent.parent

dvoice_path = os.path.join(data_path, 'data', 'dvoice.json')

dr_path = os.path.join(data_path, 'data', 'dementia_review.json')

mri_path = os.path.join(data_path, 'data', 'mri.json')

np_path = os.path.join(data_path, 'data', 'np.json')

pib_path = os.path.join(data_path, 'data', 'pib.json')

apoe_path = os.path.join(data_path, 'data', 'apoe.json')

dnp_path = os.path.join(data_path, 'data', 'dnp.json')

anon_dvoice_path = os.path.join(data_path, 'data', 'anonymized_digital_voice.json')

dcdt_path = os.path.join(data_path, 'data', 'dcdt.json')

education_path = os.path.join(data_path, 'data', 'education.json')

race_path = os.path.join(data_path, 'data', 'race_sex.json')

sex_path = os.path.join(data_path, 'data', 'race_sex.json')

tau_path = os.path.join(data_path, 'data', 'tau.json')



index = 'student-dvoice'




'''print(dates)

    # m 1
    mri_id = client.search(index='student-mri', size =10000, query=filter_mri_config.mri(idx_list))['hits']['hits']
    mri_dict = {}
    test_idx = []
    for key in mri_id:
        if key['_source']['dummy_id'] not in mri_dict:
            mri_dict[key['_source']['dummy_id']] = [key['_source']['date']]
        else:
            mri_dict[key['_source']['dummy_id']].append(key['_source']['date'])
    
    for val in dates:
        id = val['_source']['dummy_id']
        exam_time = val['_source']['date']

        if id in mri_dict:
            for date in mri_dict[id]:
                diff = abs(dp.get_diff(date, exam_time))
                if diff <= 150:
                    test_idx.append(id + '-' + date)  
                    break
                
    '''

