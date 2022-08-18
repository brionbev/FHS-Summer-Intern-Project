import json
import os,sys

import shutil

from markupsafe import escape
from pathlib import Path
from datetime import datetime,timedelta
from tokenize import blank_re
from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, url_for,Blueprint,render_template,make_response

from flask import current_app as app
from fhs_utility.save_and_log import save_log

current = os.path.dirname(os.path.abspath(__file__))
PROJECT_HOME = os.path.dirname(current)
summer_data_team = Path(current).parent.parent
sys.path.insert(1,str(summer_data_team))

from function.anonymized_digital_voice import combine_cog_data_anonymized_digital_voice
from function.digital_voice import combine_cog_data
from function.education import combine_cog_data_education
from function.pib import combine_cog_data_pib
from function.dcdt import combine_cog_data_dcdt
from function.sex import combine_cog_data_sex
from function.apoe import combine_cog_data_apoe
from function.dementia_review import combine_cog_data_dr
from function.dnp import combine_cog_data_dnp
from function.mri import combine_cog_data_mri
from function.pib import combine_cog_data_pib
from function.race import combine_cog_data_race
from function.neuropath import combine_cog_data_neuropath
from function.tau import combine_cog_data_tau
from filtering.function import filter_mri


current = os.path.dirname(os.path.abspath(__file__))
PROJECT_HOME = os.path.dirname(current)
summer_data_team = Path(current).parent.parent
sys.path.insert(1,str(summer_data_team))

# from functions.encoding import * will import all modules
# for some reason, there is still a problem with functions.encoding
# says that there is no module within the specific one we are
# trying to import
# could it be because it was imported wrong and cannot find the
# specific folder like last time?

CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER  = os.path.join(CURRENT_FOLDER, 'uploads')
ALLOWED_EXTENSIONS = set(['json','csv'])

importdata = {
    'anonymized_digital_voice': combine_cog_data_anonymized_digital_voice,
    'dvoice' :combine_cog_data,
    'apoe' :combine_cog_data_apoe,
    'anonymized_digital_voice' :combine_cog_data_anonymized_digital_voice,
    'dementia_review' :combine_cog_data_dr,
    'dnp' :combine_cog_data_dnp,
    'mri' :combine_cog_data_mri,
    'pib' :combine_cog_data_pib,
    'np' :combine_cog_data_neuropath,
    'education' :combine_cog_data_education,
    'dcdt' :combine_cog_data_dcdt,
    'sex' :combine_cog_data_sex,
    'tau':combine_cog_data_tau,
    'race_sex':combine_cog_data_sex,
    'mri_filtering':filter_mri
}
# importdata needed for the script to read which data set we want


# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates'
)



def allowed_file(filename):
    '''Makes sure the file is allowed within the search'''
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@home_bp.route("/", methods=['GET', 'POST'])
def index():
    '''Creates the index for auth and admin routes'''
    pages = []
    lastmod = datetime.now() - timedelta(days=10)
    lastmod = lastmod.strftime('%Y-%m-%d')
    for rule in app.url_map.iter_rules():
    # omit auth and admin routes and if route has parameters. Only include if route has GET method
        if 'GET' in rule.methods and len(rule.arguments) == 0:
            pages.append(['http://localhost:5001' + rule.rule, lastmod])



    sitemap_template = render_template('sitemap_t.html', pages=pages)
    response = make_response(sitemap_template)
    response.headers['Content-Type'] = 'text/html'
    return response

# dependent on what is inside of headers, it will change plus what we set it equal to as well
# is there anything else that can possibly change it



@home_bp.route('/url.css')
def css():
    response = make_response(render_template("url.css"))
    response.headers['Content-type'] = 'text/css'
    return response



@home_bp.route("/clear", methods=['GET'])
# clear() deletes what was uploaded to the folder and returns to index when done empty
def clear():
    '''Clears the folder that is currently listed'''
    folder = UPLOAD_FOLDER

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    return redirect(url_for('index'))

@home_bp.route('/<functype>/<testtype>/download')
def download(functype,testtype):

    filedata = testtype + '_bp.' + 'encode_' + testtype
    # filedata is the path of what script we want to be reading, like race, apoe, etc

    filename = request.args.get('filename')
    func = request.args.get('func')
    f_args = request.args.getlist('f_args')
    # return the appropriate script to call based on the name of the page (testtype) the request is currently being made on

    # method_to_call = getattr(combine_cog_data,func)
    # what it was originally only had hardcoded to dvoice, we want the others

    method_to_call = getattr(importdata[testtype],func)
    # gets the data of what script we want

    json_path = os.path.join(PROJECT_HOME,'downloads',functype,testtype,filename)
    #{'front_ext': 'M:\\mtao\\api_testing\\downloads\\encoding\\dvoice\\2022-06-1012-00-10.520086.csv', 'ignore_result_keys': {'_save_loc'}}
    _SAVE_LOG_KW = {'front_ext': json_path, 'ignore_result_keys': {'_save_loc'}}

    save_log(method_to_call,**_SAVE_LOG_KW)(f_args)
    # return redirect(url_for('dvoice_bp.encode_dvoice',f_args=f_args))
    return redirect(url_for(filedata,f_args=f_args))
 



# if __name__ == "__main__":
#     app.run(host='localhost', port=5001, debug=True)

# Each dataset was created an individualized route (routes_apoe, routes_np, etc)
# These routes help direct what scripts we are comparing data from to dvoice, this is
# done through home_bp.route

# When this is run, it generates and prints all what was encoded in the functions folder
# (the first part we did), in this case: apoe, dr, dvoice, dnp, mri, np, pib, race (race_sex)



#import encoding.routes_anonymized_digital_voice as anon_dvoice
#import encoding.routes_apoe as apoe
#import encoding.routes_dcdt as dcdt
#import encoding.routes_dementia_review as dr
#import encoding.routes_dnp as dnp
#import encoding.routes_dvoice as dvoice
#import encoding.routes_education as educ
#import encoding.routes_mri as mri
#import encoding.routes_np as np
#import encoding.routes_pib as pib
#import encoding.routes_race_sex as rs
#import encoding.routes_tau as tau
#import encoding.routes as routes

# scripts that corresponds to the testtype variable in the blueprint 
#encoding_dict = {'dvoice':dvoice, 'anonymized_digital_voice':anon_dvoice, 'apoe':apoe, 'dcdt':dcdt, 'dementia_review':dr, 'dnp':dnp, 'education':educ,
#'mri':mri, 'neuropath':np, 'pib':pib, 'race_sex':rs, 'tau':tau}

#from functions.events.anonymized_digital_voice import anon_dvoice_merge
#from functions.events.dcdt import dcdt_merge
#from functions.events.mri import mri_merge
#from functions.events.dnp import dnp_merge
#from functions.events.dvoice import dvoice_merge
#from functions.events.education import education_merge
#from functions.events.pib import pib_merge
#from functions.events.tau import tau_merge


#events_dict = {'events_mri':mri_merge, 'events_anon_dvoice':anon_dvoice_merge, 'events_dcdt':dcdt_merge, 'events_dnp':dnp_merge,
#'events_dvoice':dvoice_merge, 'events_education':education_merge, 'events_pib':pib_merge, 'events_tau':tau_merge}



#from functions.encoding.digital_voice import combine_cog_data
#from functions.encoding.digital_voice import combine_cog_data
#from functions.encoding.education import combine_cog_data_education
#from functions.encoding.pib import combine_cog_data_pib
#from functions.encoding.dcdt import combine_cog_data_dcdt
#from functions.encoding.sex import combine_cog_data_sex
#from functions.encoding.apoe import combine_cog_data_apoe
#from functions.encoding.dementia_review import combine_cog_data_dr
#from functions.encoding.dnp import combine_cog_data_dnp
#from functions.encoding.mri import combine_cog_data_mri
#from functions.encoding.pib import combine_cog_data_pib
#from functions.encoding.race import combine_cog_data_race
#from functions.encoding.neuropath import combine_cog_data_neuropath
