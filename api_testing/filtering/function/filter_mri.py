from multiprocessing.sharedctypes import Value
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import elasticsearch as es
from elasticsearch.helpers import scan
from fhs_utility.save_and_log import save_log
from fhs_utility.elastic import id_generator as helper
from mergedeep import merge
from filtering.function import filter_mri_config
from fhs_utility.read_pkg.read import read_dictionary_file

from fhs_utility.handle_dates import date_parse as dp

def get_id_list(data_json):
    '''Return list of keys'''
    
    return list(data_json.keys())

def intersection(*args):
    '''Creates the intersection between a list of sets'''
    return list(set.intersection(*args))

def convert_id(some_list):
    converted_list = []
    for i in some_list:
        converted_list.append(i.split('-')[0])
    return converted_list

# returns a list of ids that can be found in both mri and dvoice
stripped = []
def dates_filter(client,index, idx_list, threshold):
    '''Filter dates within 180 days'''
    if threshold[0].isdigit() is False:
        raise ValueError("Input is not a number")
    else:
        threshold = abs(int(threshold[0]))

    dates = client.search(index=index, size =1000, query={'terms': {'_id' : idx_list}})['hits']['hits']
    mri = client.search(index='student-mri', size=10000, query=filter_mri_config.mri(dates))['hits']['hits']
    new_idx = []

    mri_dic = {key['_id']:[] for key in dates} 
    mri_freq = {key['_id']:0 for key in mri} 
    dic = {key['_source']['dummy_id']:[] for key in dates} 
    for key in dates:
        dic[key['_source']['dummy_id']].append(key['_source']['date'])

    for item in mri:
        id = item['_id']
        dummy = item['_source']['dummy_id']
        date = item['_source']['date']

        for time in dic[dummy]:
            diff = abs(dp.get_diff(time, date))
            dvoice_id = str(dummy + '-' + time) 
            if (diff <= threshold):
                mri_freq[id] = mri_freq[id] + 1
                
                temp = [val for val in mri_dic[dvoice_id]]
                temp.append(id)
                mri_dic[dvoice_id] = temp

    for key in mri_dic:
        if mri_dic[key] != []:
            max_freq = mri_dic[key][0]
            for item in mri_dic[key]:
                if mri_freq[item] > mri_freq[max_freq]:
                    max_freq = item
            new_idx.append(max_freq)
    
    #print(len(new_idx))
    print('test len: ' + str(len(new_idx)))
    return new_idx

def gen_combined(threshold):
    '''Merges using mask of shared IDs'''
    
    helper.make_client(filter_mri_config.auth) # id generator; auth = ('student','fhs1234')
    client = helper.get_client()  # acquire the client <Elasticsearch(['https://192.168.1.175:9200'])>
    index = filter_mri_config.index # index = 'student-dvoice'

    # create a list that contains two sets, one for the ids of 'student-dvoice', one for the ids of 'student-mri'
    # also the line of code that took the longest amounts of time to run
    idx_list = list(set(dates_filter(client, index, helper.query_ids(client,index), threshold)) & set(helper.query_ids(client,'student-mri')))

    dvoice_resp = client.search(index=index, size = 1000, query = {'terms': {'_id' : idx_list}})['hits']['hits']
    mri_resp = client.search(index='student-mri', size = 2000, query = {'terms': {'_id' : idx_list}})['hits']['hits']
    
    dvoice_dict = {key['_id']:key['_source'] for key in dvoice_resp}
    mri_dict = {key['_id']:key['_source'] for key in mri_resp}
    
    return {'final': merge(dvoice_dict,mri_dict)}

print(len(gen_combined(['180'])['final']))

#def main():
#    '''Prints log file generates json'''
#    gen_combined(['180'])

#if __name__ == '__main__':
#    main()

#test_result = gen_combined()
#print((test_result['final']))


#from filter_test import true_result
#exp_result = gen_combined()
#print(exp_result == true_result)

