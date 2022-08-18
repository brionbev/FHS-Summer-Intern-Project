import datetime
from flask import request, redirect, url_for,Blueprint



dvoice_bp = Blueprint(
    'dvoice_bp', __name__,
)


@dvoice_bp.route("/encoding/dvoice",methods=['GET','POST'])
def encode_dvoice():
    tests = request.form.getlist('tests')

    if (request.method == 'POST') & bool(tests):
    
        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')

        data = {'filename':filename,'func': 'encode', 'f_args': tests}

        return redirect(url_for('home_bp.download', functype='encoding', testtype = 'education', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
    <h2> Select encoding data for Digital Voice </h2>
<input type="checkbox" name="tests" value="anonymized_digital_voice" unchecked> anonymized dvoice </br>
<input type="checkbox" name="tests" value="apoe" unchecked> apoe </br>
<input type="checkbox" name="tests" value="dcdt" unchecked> dcdt </br>
<input type="checkbox" name="tests" value="dementia_review" unchecked> dementia_review </br>
<input type="checkbox" name="tests" value="dnp" unchecked> dnp </br>
<input type="checkbox" name="tests" value="dvoice" unchecked> dvoice </br>
<input type="checkbox" name="tests" value="education" unchecked> education </br>
<input type="checkbox" name="tests" value="mri" unchecked> mri </br>
<input type="checkbox" name="tests" value="np" unchecked> np </br>
<input type="checkbox" name="tests" value="pib" unchecked> pib </br>
<input type="checkbox" name="tests" value="race_sex" unchecked> race_sex </br>
<input type="checkbox" name="tests" value="tau" unchecked> tau </br>
<input type="submit">
</form>
<form action="http://localhost:5001">
<input type="submit" value="Back to links"/>
</form>
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)
