from flask import Blueprint
from app.models import Artifact

artifact_routes = Blueprint('artifacts', __name__)


@artifact_routes.route('/')
def artifacts():
    artifacts = Artifact.query.all()
    return {'artifacts': [artifact.to_dict() for artifact in artifacts]}
