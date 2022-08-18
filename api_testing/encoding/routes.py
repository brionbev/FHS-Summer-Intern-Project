import datetime
from flask import request, redirect, url_for,Blueprint

anonymized_digital_voice_bp = Blueprint(
    'anonymized_digital_voice_bp', __name__,
)

apoe_bp = Blueprint(
    'apoe_bp',__name__,
)

dcdt_bp = Blueprint(
    'dcdt_bp', __name__,
)

dementia_review_bp = Blueprint(
    'dementia_review_bp', __name__,
)

dvoice_bp = Blueprint(
    'dvoice_bp', __name__,
)

dnp_bp = Blueprint(
    'dnp_bp', __name__,
)

education_bp = Blueprint(
    'education_bp', __name__,
)

mri_bp = Blueprint(
    'mri_bp', __name__,
)

neuropath_bp = Blueprint(
    'neuropath_bp', __name__,
)

pib_bp = Blueprint(
    'pib_bp', __name__,
)

race_bp = Blueprint(
    'race_bp', __name__,
)

sex_bp = Blueprint(
    'sex_bp', __name__,
)

tau_bp = Blueprint(
    'tau_bp', __name__,
)
    

@anonymized_digital_voice_bp.route("/encoding/anonymized_digital_voice", methods=['GET', 'POST'])
def encode_anonymized_digital_voice():
    tests = request.form.getlist('tests')
    
    if (request.method == 'POST') & bool(tests):
    

        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')

        data = {'filename':filename,'func': 'encode', 'f_args': tests}


        return redirect(url_for('home_bp.download', functype='encoding', testtype = 'anonymized_digital_voice', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
    <h2> Select encoding data for Anonymized Digital Voice </h2>
<input type="checkbox" name="tests" value="anon_dvoice" unchecked> anonymized_dvoice </br>
<input type="checkbox" name="tests" value="apoe" unchecked> apoe </br>
<input type="checkbox" name="tests" value="dcdt" unchecked> dcdt </br>
<input type="checkbox" name="tests" value="dr" unchecked> dementia_review </br>
<input type="checkbox" name="tests" value="dnp" unchecked> dnp </br>
<input type="checkbox" name="tests" value="dvoice" unchecked> dvoice </br>
<input type="checkbox" name="tests" value="educ" unchecked> education </br>
<input type="checkbox" name="tests" value="mri" unchecked> mri </br>
<input type="checkbox" name="tests" value="np" unchecked> np </br>
<input type="checkbox" name="tests" value="pib" unchecked> pib </br>
<input type="checkbox" name="tests" value="rs" unchecked> race_sex </br>
<input type="checkbox" name="tests" value="tau" unchecked> tau </br>
<input type="submit">
</form>
<form action="http://localhost:5001">
<input type="submit" value="Back to links"/>
</form>
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@apoe_bp.route("/encoding/apoe", methods=['GET', 'POST'])
def encode_apoe():
    tests = request.form.getlist('tests')
    
    if (request.method == 'POST') & bool(tests):
    

        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')

        data = {'filename':filename,'func': 'encode', 'f_args': tests}


        return redirect(url_for('home_bp.download', functype='encoding', testtype = 'apoe', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
    <h2> Select encoding data for APOE </h2>
<input type="checkbox" name="tests" value="anon_dvoice" unchecked> anonymized_dvoice </br>
<input type="checkbox" name="tests" value="apoe" unchecked> apoe </br>
<input type="checkbox" name="tests" value="dcdt" unchecked> dcdt </br>
<input type="checkbox" name="tests" value="dr" unchecked> dementia_review </br>
<input type="checkbox" name="tests" value="dnp" unchecked> dnp </br>
<input type="checkbox" name="tests" value="dvoice" unchecked> dvoice </br>
<input type="checkbox" name="tests" value="educ" unchecked> education </br>
<input type="checkbox" name="tests" value="mri" unchecked> mri </br>
<input type="checkbox" name="tests" value="np" unchecked> np </br>
<input type="checkbox" name="tests" value="pib" unchecked> pib </br>
<input type="checkbox" name="tests" value="rs" unchecked> race_sex </br>
<input type="checkbox" name="tests" value="tau" unchecked> tau </br>
<input type="submit">
</form>
<form action="http://localhost:5001">
<input type="submit" value="Back to links"/>
</form>
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@dcdt_bp.route("/encoding/dcdt", methods=['GET', 'POST'])
def encode_dcdt():
    tests = request.form.getlist('tests')
    
    if (request.method == 'POST') & bool(tests):
    

        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')

        data = {'filename':filename,'func': 'encode', 'f_args': tests}


        return redirect(url_for('home_bp.download', functype='encoding', testtype = 'dcdt', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
<input type="checkbox" name="tests" value="anon_dvoice" unchecked> anonymized dvoice </br>
<input type="checkbox" name="tests" value="apoe" unchecked> apoe </br>
<input type="checkbox" name="tests" value="dcdt" unchecked> dcdt </br>
<input type="checkbox" name="tests" value="dr" unchecked> dementia_review </br>
<input type="checkbox" name="tests" value="dnp" unchecked> dnp </br>
<input type="checkbox" name="tests" value="dvoice" unchecked> dvoice </br>
<input type="checkbox" name="tests" value="educ" unchecked> education </br>
<input type="checkbox" name="tests" value="mri" unchecked> mri </br>
<input type="checkbox" name="tests" value="np" unchecked> np </br>
<input type="checkbox" name="tests" value="pib" unchecked> pib </br>
<input type="checkbox" name="tests" value="rs" unchecked> race_sex </br>
<input type="checkbox" name="tests" value="tau" unchecked> tau </br>
<input type="submit">
</form>
<form action="http://localhost:5001">
<input type="submit" value="Back to links"/>
</form>
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@dementia_review_bp.route("/encoding/dementia_review", methods=['GET', 'POST'])
def encode_dementia_review():
    tests = request.form.getlist('tests')
    
    if (request.method == 'POST') & bool(tests):
    

        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')

        data = {'filename':filename,'func': 'encode', 'f_args': tests}


        return redirect(url_for('home_bp.download', functype='encoding', testtype = 'dementia_review', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
<input type="checkbox" name="tests" value="anon_dvoice" unchecked> anonymized dvoice </br>
<input type="checkbox" name="tests" value="apoe" unchecked> apoe </br>
<input type="checkbox" name="tests" value="dcdt" unchecked> dcdt </br>
<input type="checkbox" name="tests" value="dr" unchecked> dementia_review </br>
<input type="checkbox" name="tests" value="dnp" unchecked> dnp </br>
<input type="checkbox" name="tests" value="dvoice" unchecked> dvoice </br>
<input type="checkbox" name="tests" value="educ" unchecked> education </br>
<input type="checkbox" name="tests" value="mri" unchecked> mri </br>
<input type="checkbox" name="tests" value="np" unchecked> np </br>
<input type="checkbox" name="tests" value="pib" unchecked> pib </br>
<input type="checkbox" name="tests" value="rs" unchecked> race_sex </br>
<input type="checkbox" name="tests" value="tau" unchecked> tau </br>
<input type="submit">
</form>
<form action="http://localhost:5001">
<input type="submit" value="Back to links"/>
</form>
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@dvoice_bp.route("/encoding/dvoice",methods=['GET','POST'])
def encode_dvoice():
    '''Provides GUI and I/O for encoding digital voice script'''
    tests = request.form.getlist('tests')
    if (request.method == 'POST') & bool(tests):


        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')

        data = {'filename':filename,'func': 'encode', 'f_args': tests}


        return redirect(url_for('home_bp.download', functype='encoding', testtype = 'dvoice', **data))

    submitted = request.args.getlist('f_args')

    return '''<form method="post">
    <h2> Select encoding data for digital voice </h2>
<input type="checkbox" name="tests" value="anon_dvoice" unchecked> anonymized dvoice </br>
>>>>>>> 99e80274c55e54f926d0878c2a643375a643bf6f
<input type="checkbox" name="tests" value="apoe" unchecked> apoe </br>
<input type="checkbox" name="tests" value="dcdt" unchecked> dcdt </br>
<input type="checkbox" name="tests" value="dr" unchecked> dementia_review </br>
<input type="checkbox" name="tests" value="dnp" unchecked> dnp </br>
<input type="checkbox" name="tests" value="dvoice" unchecked> dvoice </br>
<input type="checkbox" name="tests" value="educ" unchecked> education </br>
<input type="checkbox" name="tests" value="mri" unchecked> mri </br>
<input type="checkbox" name="tests" value="np" unchecked> np </br>
<input type="checkbox" name="tests" value="pib" unchecked> pib </br>
<input type="checkbox" name="tests" value="rs" unchecked> race_sex </br>
<input type="checkbox" name="tests" value="tau" unchecked> tau </br>
<input type="submit">
</form>
<form action="http://localhost:5001">
<input type="submit" value="Back to links"/>
</form>
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

# Each one of these routes map to a specific blueprint (in this case, dvoice) it takes the time
# and date of today when it is being called

