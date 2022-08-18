'''Environmental variables for elastic importing'''

from pathlib import Path
import os


data_path = Path('.').absolute().parent.parent.parent

dvoice_path = os.path.join(data_path, 'data', 'dvoice_dummy.json')

dr_path = os.path.join(data_path, 'bbrion','data', 'dementia_review_dummy.json')

mri_path = os.path.join(data_path, 'data', 'mri_dummy.json')

np_path = os.path.join(data_path, 'data', 'np_dummy.json')

pib_path = os.path.join(data_path, 'data', 'pib_dummy.json')

apoe_path = os.path.join(data_path, 'data', 'apoe_dummy.json')

dnp_path = os.path.join(data_path, 'data', 'dnp_dummy.json')

anon_dvoice_path = os.path.join(data_path, 'data', 'anonymized_digital_voice_dummy.json')

dcdt_path = os.path.join(data_path, 'bbrion', 'data', 'dcdt_dummy.json')

education_path = os.path.join(data_path, 'data', 'education_dummy.json')

race_sex_path = os.path.join(data_path, 'data', 'race_sex_dummy.json')

tau_path = os.path.join(data_path, 'data', 'tau_dummy.json')
