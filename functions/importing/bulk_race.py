import json
import elasticsearch as es
from elasticsearch.helpers import streaming_bulk
import tqdm

import fhs_utility.elastic.bulk_import as bulk
import importing_config

kwargs = {
        'datefield' : 'race1',
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


data_path = importing_config.race_path

bulk.import_data(('student', 'fhs1234'), None,'student-race_sex', data_path, **kwargs)

