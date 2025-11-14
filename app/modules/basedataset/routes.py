from flask import render_template
from app.modules.basedataset import basedataset_bp


@basedataset_bp.route('/basedataset', methods=['GET'])
def index():
    return render_template('basedataset/index.html')
