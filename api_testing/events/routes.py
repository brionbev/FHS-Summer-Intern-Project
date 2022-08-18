import datetime
from flask import request, redirect, url_for,Blueprint


events_anon_dvoice_bp = Blueprint(
    'events_anon_dvoice_bp', __name__,
)

events_dcdt_bp = Blueprint(
    'events_dcdt_bp', __name__,
)

events_dnp_bp = Blueprint(
    'events_dnp_bp', __name__
)

events_dvoice_bp = Blueprint(
    'events_dvoice_bp', __name__
)

events_education_bp = Blueprint(
    'events_education_bp', __name__
)

events_mri_bp = Blueprint(
    'events_mri_bp', __name__,
)

events_pib_bp = Blueprint(
    'events_pib_bp', __name__
)

events_tau_bp = Blueprint(
    'events_tau_bp', __name__
)

@events_anon_dvoice_bp.route('/events/anonymized_digital_voice', methods=['GET','POST'])
def events_anon_dvoice():
    tests = request.form.getlist('tests')
    if (request.method == 'POST') & bool(tests):
        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')
        data = {'filename':filename,'func': 'encode', 'f_args': tests}
        return redirect(url_for('home_bp.download', functype='events', testtype = 'events_anon_dvoice', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
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
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@events_dcdt_bp.route('/events/dcdt', methods=['GET','POST'])
def events_dcdt():
    tests = request.form.getlist('tests')
    if (request.method == 'POST') & bool(tests):
        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')
        data = {'filename':filename,'func': 'encode', 'f_args': tests}
        return redirect(url_for('home_bp.download', functype='events', testtype = 'events_dcdt', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
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
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@events_dnp_bp.route('/events/dnp', methods=['GET','POST'])
def events_dnp():
    tests = request.form.getlist('tests')
    if (request.method == 'POST') & bool(tests):
        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')
        data = {'filename':filename,'func': 'encode', 'f_args': tests}
        return redirect(url_for('home_bp.download', functype='events', testtype = 'events_dnp', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
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
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@events_dvoice_bp.route('/events/dvoice', methods=['GET','POST'])
def events_dvoice():
    tests = request.form.getlist('tests')
    if (request.method == 'POST') & bool(tests):
        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')
        data = {'filename':filename,'func': 'encode', 'f_args': tests}
        return redirect(url_for('home_bp.download', functype='events', testtype = 'events_dvoice', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
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
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@events_education_bp.route('/events/education', methods=['GET','POST'])
def events_education():
    tests = request.form.getlist('tests')
    if (request.method == 'POST') & bool(tests):
        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')
        data = {'filename':filename,'func': 'encode', 'f_args': tests}
        return redirect(url_for('home_bp.download', functype='events', testtype = 'events_education', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
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
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@events_mri_bp.route("/events/mri", methods=['GET','POST'])
def events_mri():
    tests = request.form.getlist('tests')
    if (request.method == 'POST') & bool(tests):
        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')
        data = {'filename':filename,'func': 'encode', 'f_args': tests}
        return redirect(url_for('home_bp.download', functype='events', testtype = 'events_mri', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
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
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@events_pib_bp.route("/events/pib", methods=['GET','POST'])
def events_pib():
    tests = request.form.getlist('tests')
    if (request.method == 'POST') & bool(tests):
        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')
        data = {'filename':filename,'func': 'encode', 'f_args': tests}
        return redirect(url_for('home_bp.download', functype='events', testtype = 'events_pib', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
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
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

@events_tau_bp.route("/events/tau", methods=['GET','POST'])
def events_tau():
    tests = request.form.getlist('tests')
    if (request.method == 'POST') & bool(tests):
        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')
        data = {'filename':filename,'func': 'encode', 'f_args': tests}
        return redirect(url_for('home_bp.download', functype='events', testtype = 'events_tau', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
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
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)