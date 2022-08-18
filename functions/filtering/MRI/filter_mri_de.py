from cgi import test
import os
from numpy import true_divide
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import elasticsearch as es
from elasticsearch.helpers import scan
from fhs_utility.save_and_log import save_log
from fhs_utility.elastic import id_generator as helper
from mergedeep import merge
import filter_mri_config

from fhs_utility.read_pkg.read import read_dictionary_file
from fhs_utility.handle_dates import date_parse as dp
#from filter_mri import stripped
#from filter_mri import test_result


repeat = ['FHS_ES00770-20201118', 'FHS_ES00826-20210114', 'FHS_ES01612-20210102', 
'FHS_ES01731-20210407', 'FHS_ES01748-20210130', 'FHS_ES02607-20210213', 
'FHS_ES03059-20210312', 'FHS_ES03470-20210316', 'FHS_ES03812-20210323', 
'FHS_ES03855-20200915', 'FHS_ES04206-20201207', 'FHS_ES04224-20210115', 'FHS_ES04277-20210116', 
'FHS_ES04431-20210316', 'FHS_ES04489-20200908', 'FHS_ES04534-20210131', 'FHS_ES04567-20210228', 
'FHS_ES04609-20210303', 'FHS_ES04634-20201216', 'FHS_ES05096-20201201', 'FHS_ES05096-20201201', 'FHS_ES05165-20201117',
 'FHS_ES05344-20210202', 'FHS_ES05346-20210109', 'FHS_ES05510-20200815', 'FHS_ES05510-20200815', 'FHS_ES05569-20201117', 
 'FHS_ES05726-20210109', 'FHS_ES05726-20210109', 'FHS_ES05762-20210301', 'FHS_ES06197-20201126', 'FHS_ES06728-20210207', 
 'FHS_ES07257-20201127', 'FHS_ES08516-20210121', 'FHS_ES08956-20210116', 'FHS_ES09224-20210323', 'FHS_ES09327-20210109', 
 'FHS_ES09439-20210216', 'FHS_ES09923-20210217', 'FHS_ES10245-20210121', 'FHS_ES10784-20210320', 'FHS_ES11100-20201008', 
 'FHS_ES11630-20200930', 'FHS_ES12488-20210502', 'FHS_ES12526-20210129', 'FHS_ES12587-20210228', 'FHS_ES12607-20210104', 
 'FHS_ES12971-20200731', 'FHS_ES13009-20201208', 'FHS_ES13379-20201218', 'FHS_ES13565-20210228', 'FHS_ES13709-20210129', 
 'FHS_ES14266-20210129', 'FHS_ES14415-20201128', 'FHS_ES14415-20201128', 'FHS_ES14565-20210118', 'FHS_ES14689-20201112', 
 'FHS_ES14882-20201206', 'FHS_ES14882-20201206', 'FHS_ES15367-20200808', 'FHS_ES15586-20201120', 'FHS_ES15643-20200816', 'FHS_ES15643-20200816', 'FHS_ES16096-20210124', 'FHS_ES16619-20201210', 'FHS_ES17225-20201102', 'FHS_ES17354-20210209', 'FHS_ES17471-20210123', 'FHS_ES17798-20210315', 'FHS_ES18058-20210122', 'FHS_ES18541-20210218', 'FHS_ES18667-20210416', 'FHS_ES18798-20210129', 'FHS_ES18798-20210129', 'FHS_ES19083-20210119', 'FHS_ES19244-20200920', 'FHS_ES19339-20210107', 'FHS_ES19436-20210322', 'FHS_ES19436-20210322', 'FHS_ES20542-20210215', 'FHS_ES20659-20201127', 'FHS_ES20701-20210117', 'FHS_ES20792-20210211', 'FHS_ES20859-20210319', 'FHS_ES21623-20210310', 'FHS_ES21671-20210215', 'FHS_ES21802-20200820', 'FHS_ES22149-20210213', 'FHS_ES22242-20210112', 'FHS_ES22242-20210112', 'FHS_ES22347-20210117', 'FHS_ES22405-20200805', 'FHS_ES22641-20210302', 'FHS_ES22711-20201213', 'FHS_ES22718-20210214', 'FHS_ES22864-20201225', 'FHS_ES23266-20201114', 'FHS_ES23481-20201209', 'FHS_ES23560-20210116', 'FHS_ES23745-20201116', 'FHS_ES24149-20210215', 'FHS_ES24982-20210219', 'FHS_ES25027-20210104', 'FHS_ES25186-20201108', 'FHS_ES25386-20210227', 
 'FHS_ES25488-20210121', 'FHS_ES25805-20210212', 'FHS_ES26169-20210403', 'FHS_ES26488-20201206', 'FHS_ES26763-20210123', 'FHS_ES26765-20210130', 'FHS_ES26934-20210129', 'FHS_ES27282-20210119', 'FHS_ES27757-20210422', 'FHS_ES27900-20210121', 'FHS_ES28156-20200822', 'FHS_ES28426-20210208', 'FHS_ES28464-20201202', 'FHS_ES28593-20210130', 'FHS_ES28676-20200822', 'FHS_ES28676-20200822', 'FHS_ES28907-20210315', 'FHS_ES29217-20210325', 'FHS_ES29463-20210114', 'FHS_ES29638-20210310', 'FHS_ES30447-20201231', 'FHS_ES30474-20210304']

rep = {key.split('-')[0]:'' for key in repeat}

def get_id_list(data_json):
    '''Return list of keys'''
    return list(data_json.keys())


def intersection(*args):
    '''Creates the intersection between a list of sets'''
    return list(set.intersection(*args))

true_stripped = []
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


#if __name__ == '__main__':
#    main()

true_result = gen_combined()

print((true_result['final']))

#print('stripped: ' + str(len(stripped)))
#print('true stripped: ' + str(len(true_stripped)))





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