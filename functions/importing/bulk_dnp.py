import json
import elasticsearch as es
from elasticsearch.helpers import streaming_bulk
import tqdm

import fhs_utility.elastic.bulk_import as bulk
import importing_config

kwargs = {
        'datefield' : 'date',
        'settings': {
        'number_of_shards' : 3,
        },
        'mappings' : {
        'dynamic' : 'true',
        'properties' : {
                'date' : {
                        'type' : 'date',
                        'format' : 'yyyyMMdd'
                }
        }
        }
}


data_path = importing_config.dnp_path
bulk.import_data(('student', 'fhs1234'), None,'student-dnp', data_path, **kwargs)

#sets up the format for importing the json files, changes according to type of data
#i.e. anon_dvoice uses the date as one of the objects within the json file therefore
#we set it up using datefield and date
#i.e. dvoice uses data within the json file and needs the data_object along with dvoice_data
#in order to access the data within the json file
