import json
import elasticsearch as es
from elasticsearch.helpers import streaming_bulk
import tqdm

import fhs_utility.elastic.bulk_import as bulk
import importing_config


kwargs = {
        'datefield' : 'cohort',
        'settings': {
        'number_of_shards' : 3,
        },
        'mappings' : {
        'dynamic' : 'true',
        'properties' : {
        }
        }
        
}

#setting datefield as cohort or dummy_id allows the file to obtain the information within 
#the data files; this happens because cohort acts as a datefield within dr or np in which
#both json files do not contain dates in either file

data_path = importing_config.np_path

bulk.import_data(('student', 'fhs1234'), None,'student-np', data_path, **kwargs)

#sets up the format for importing the json files, changes according to type of data
#i.e. anon_dvoice uses the date as one of the objects within the json file therefore
#we set it up using datefield and date
#i.e. dvoice uses data within the json file and needs the data_object along with dvoice_data
#in order to access the data within the json file
