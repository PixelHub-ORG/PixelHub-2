from flask import Blueprint
from fakenodo.blueprints.depositions import depositions_bp

api_bp = Blueprint("api_bp", __name__)

# Registrar blueprints
api_bp.register_blueprint(depositions_bp, url_prefix='/depositions')