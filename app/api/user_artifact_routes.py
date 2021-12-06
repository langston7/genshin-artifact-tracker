from flask import Blueprint
from app.models import User_Artifact

user_artifact_routes = Blueprint('user_artifacts', __name__)


@user_artifact_routes.route('/')
def user_artifacts():
    user_artifacts = User_Artifact.query.all()
    return {'user_artifacts': [user_artifact.to_dict() for user_artifact in user_artifacts]}


@user_artifact_routes.route('/<int:user_id>')
def one_users_artifacts(user_id):
    user_artifacts = User_Artifact.query.filter(User_Artifact.user_id == user_id).first()
    user_artifacts = User_Artifact.query.all()
    return {'user_artifacts': [user_artifact.to_dict() for user_artifact in user_artifacts]}
