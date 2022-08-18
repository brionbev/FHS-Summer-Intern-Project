'''Environmental variables for combine cog data'''

import os
from pathlib import Path



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

race_sex_path = os.path.join(data_path, 'data', 'race_sex.json')

tau_path = os.path.join(data_path, 'data', 'tau.json')
