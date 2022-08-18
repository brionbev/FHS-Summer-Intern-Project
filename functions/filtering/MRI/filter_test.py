from cgi import test
import os
from numpy import true_divide
import urllib3

from functions.filtering.MRI.filter_mri_config import date_query
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import elasticsearch as es
from elasticsearch.helpers import scan
from fhs_utility.save_and_log import save_log
from fhs_utility.elastic import id_generator as helper
from mergedeep import merge
import filter_mri_config

from fhs_utility.read_pkg.read import read_dictionary_file
from fhs_utility.handle_dates import date_parse as dp
from filter_mri import stripped



def get_id_list(data_json):
    '''Return list of keys'''
    return list(data_json.keys())



def intersection(*args):
    '''Creates the intersection between a list of sets'''
    return list(set.intersection(*args))

true_stripped = []
hits = []
def dates_filter(client,index, idx_list):
    '''Filter dates within 180 days'''
    dates = client.search(index=index, size = 1000, query = {'terms': {'_id' : idx_list}})['hits']['hits']

    new_idx = []
    for value in dates:
        # find whether this dvoice id exists, and if it do, test whether if its
        # corresponding mri id's dates exists within the accepted range
        query = filter_mri_config.date_query(value)
        resp = client.search(index='student-mri', size=10000, query = query)

        # if the above condition is met, then append the mri id along with its date
        if resp['hits']['max_score'] is not None:    
            x = resp['hits']['hits'][0]['_id']
            new_idx.append(resp['hits']['hits'][0]['_id'])
            true_stripped.append(['dvoice ' + value['_id'], 'mri ' + x])    
            
        
    #print(new_idx)
    print('true len: ' + str(len(new_idx)))
    return new_idx


def convert_id(some_list):
    converted_list = []
    for i in some_list:
        converted_list.append(i.split('-')[0])
    return converted_list

def gen_combined():
    '''Merges using mask of shared IDs'''
    
    helper.make_client(filter_mri_config.auth)
    client = helper.get_client()

    index = filter_mri_config.index

    idx_list = list(set(dates_filter(client, index, helper.query_ids(client,index))) & set(helper.query_ids(client,'student-mri')))
    
    dvoice_resp = client.search(index='student-dvoice', size = 1000, query = {'terms': {'_id' : idx_list}})['hits']['hits']
    mri_resp = client.search(index='student-mri', size = 2000, query = {'terms': {'_id' : idx_list}})['hits']['hits']
    dvoice_dict = {}
    for exam in dvoice_resp:
        dvoice_dict[exam['_id']] = exam['_source']
    mri_dict = {}
    for exam in mri_resp:
        mri_dict[exam['_id']] = exam['_source']


    return {'final': merge(dvoice_dict,mri_dict)}



def main():
    '''Prints log file generates json'''
    gen_combined()


if __name__ == '__main__':
    main()

true_result = gen_combined()

print(len(true_result['final']))

print(len(stripped))
print(len(true_stripped))
mismatched = []
for idx, val in enumerate(stripped):
    if val[-1] != true_stripped[idx][-1]:
        merged = [['test', val],['true', true_stripped[idx]]]
        mismatched.append(merged)

mismatched = sorted(mismatched, key=lambda mismatched:mismatched[0][1][0])
#print(*mismatched, sep='\n')
print(len(mismatched))
print(hits)

#incorrect = []
#for key in test_result['final']:
#    if true_result.get(key) is None:
#        incorrect.append([key, 
#        abs(dp.get_diff(key.split('-')[1], test_result['final'][key]['date']))])
# print(incorrect)    

# notes about filtering:
# starts with getting the id lists that returns a list of keys
# then creates and intersection between a lists of sets
# moves to filter dates within 180 days
# then converts the ids
# takes mask of shared ids and merges them
# i think it looks at ids that are the same within two sets of data
# merges those ids that are the same 
# this example is mri with dvoice
# after this, prints a new json file that contains new data
# that data being mri and dvoice