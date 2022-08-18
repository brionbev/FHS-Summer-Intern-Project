import datetime
from flask import request, redirect, url_for,Blueprint

mri_filtering_bp = Blueprint(
    'mri_filtering_bp', __name__,
)

@mri_filtering_bp.route("/filtering/mri",methods=['GET','POST'])
def encode_mri_filtering():
    text = request.form.getlist('text')
    if (request.method == 'POST') & bool(text):

        today = str(datetime.datetime.now())
        filename = ((today + '.csv').replace(' ', '')).replace(':','-')

        data = {'filename':filename,'func': 'gen_combined', 'f_args': text}

        return redirect(url_for('home_bp.download', functype='filtering', testtype = 'mri_filtering', **data))

    submitted = request.args.getlist('f_args')
    return '''<form method="post">
    <input name = 'text'> range in days </br>
<input type="submit">
</form>
<form action="http://localhost:5001">
<input type="submit" value="Back to links"/>
</form>
<p>Submitted: {submitted}</p>'''.format(submitted=submitted)

