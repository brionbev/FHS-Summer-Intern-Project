'''Environmental variables for elastic importing'''

from pathlib import Path
import os

# data_path = Path(Path('.').absolute().parent.parent.parent, 'data')

data_path = Path('.').absolute().parent.parent.parent

dvoice_path = os.path.join(data_path, 'bbrion', 'data', 'dvoice_dummy.json')

dr_path = os.path.join(data_path, 'bbrion', 'data', 'dementia_review_dummy.json')

mri_path = os.path.join(data_path, 'bbrion', 'data', 'mri_dummy.json')

np_path = os.path.join(data_path, 'bbrion', 'data', 'np_dummy.json')

pib_path = os.path.join(data_path, 'bbrion', 'data', 'pib_dummy.json')

apoe_path = os.path.join(data_path, 'bbrion', 'data', 'apoe_dummy.json')

dnp_path = os.path.join(data_path, 'bbrion', 'data', 'dnp_dummy.json')

anon_dvoice_path = os.path.join(data_path, 'bbrion', 'data', 'anonymized_digital_voice_dummy.json')

dcdt_path = os.path.join(data_path, 'bbrion', 'data', 'dcdt_dummy.json')

education_path = os.path.join(data_path, 'bbrion', 'data', 'education_dummy.json')

race_sex_path = os.path.join(data_path, 'bbrion', 'data', 'race_sex_dummy.json')

sex_path = os.path.join(data_path, 'bbrion', 'data', 'race_sex_dummy.json')

tau_path = os.path.join(data_path, 'bbrion', 'data', 'tau_dummy.json')