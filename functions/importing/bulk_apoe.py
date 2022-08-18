import json

import elasticsearch as es
import fhs_utility.elastic.bulk_import as bulk
import tqdm
from elasticsearch.helpers import streaming_bulk

import importing_config
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


kwargs = {
        'datefield' : 'apoe', 
        'settings': {
        'number_of_shards' : 3,
        },
        'mappings' : {
        'dynamic' : 'true',
        'properties' : {
                
        }
        }
}



data_path = importing_config.apoe_path

bulk.import_data(('student', 'fhs1234'), None,'student-apoe', data_path, **kwargs)