"""Initialize Flask app."""
import os
from flask import Flask
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER  = os.path.join(CURRENT_FOLDER, 'uploads')


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    
    with app.app_context():
        # Import parts of our application

        from home.routes import home_bp
        from encoding.routes import anonymized_digital_voice_bp
        from encoding.routes import apoe_bp
        from encoding.routes_dcdt import dcdt_bp
        from encoding.routes_dementia_review import dementia_review_bp
        from encoding.routes_dvoice import dvoice_bp
        from encoding.routes_np import np_bp
        from encoding.routes_race_sex import race_sex_bp
        from encoding.routes_dnp import dnp_bp
        from encoding.routes_education import education_bp
        from encoding.routes_mri import mri_bp
        from encoding.routes_pib import pib_bp
        from encoding.routes_tau import tau_bp
        from filtering.route.routes_filtering import mri_filtering_bp
        
        # Register Blueprints
        app.register_blueprint(home_bp)
        app.register_blueprint(anonymized_digital_voice_bp)
        app.register_blueprint(apoe_bp)
        app.register_blueprint(dcdt_bp)
        app.register_blueprint(dementia_review_bp)
        app.register_blueprint(dvoice_bp)
        app.register_blueprint(np_bp)
        app.register_blueprint(race_sex_bp)
        app.register_blueprint(dnp_bp)
        app.register_blueprint(education_bp)
        app.register_blueprint(mri_bp)
        app.register_blueprint(pib_bp)
        app.register_blueprint(tau_bp)

        app.register_blueprint(mri_filtering_bp)
        return app




if __name__ == "__main__":
    script = create_app()
    script.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    script.run(host='localhost', port=5001, debug=True)

# Observation notes when running:
# mri, dvoice, dnp, and dcdt are the only ones that produce outputs of 1
# pib has only one 1 (does have a smaller data set)
# Manually checked a few and it matched up
# anon dvoice, apoe, dr, education, np, race, sex, tau all produce outputs of -1
# Is this because there are no matches for these or is there a bug?

# When __init__ is run it takes the arguments of whatever scripts chosen on
# localhost, creates a csv file with today's date and time it was run, runs
# the function encode, and saves what was run in a downloads folder
# The ouput produced are 1s and -1s to see if the same particpants appear in dvoice and the
# the ones that were chosen

# Tested with dummy data - produces wrong output (-1), except when tested with self