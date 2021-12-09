from flask import Blueprint
from app.models import User_Artifact, Artifact
from sqlalchemy import or_

user_artifact_routes = Blueprint('user_artifacts', __name__)


@user_artifact_routes.route('/')
def user_artifacts():
    user_artifacts = User_Artifact.query.all()
    return {'user_artifacts': [user_artifact.to_dict() for user_artifact in user_artifacts]}


@user_artifact_routes.route('/<int:user_id>')
def one_users_artifacts(user_id):
    user_artifacts = User_Artifact.query.filter(User_Artifact.user_id == user_id).all()
    return {'user_artifacts': [user_artifact.to_dict() for user_artifact in user_artifacts]}


@user_artifact_routes.route('/<int:user_id>/dataForMainStatChart')
def data_for_main_stat_chart(user_id):
    user_artifacts = User_Artifact.query.filter(User_Artifact.user_id == user_id).all()
    countOfStatsDict = {
        'HP': 0,
        'ATK': 0,
        'HP%': 0,
        'ATK%': 0,
        'DEF%': 0,
        'Energy Recharge': 0,
        'Elemental Mastery': 0,
        'PHYS%': 0,
        'ELEM%': 0,
        'CRIT RATE': 0,
        'CRIT DMG': 0,
    }
    for artifact in user_artifacts:
        countOfStatsDict[artifact.primary_stat]+=1

    primaryStats = countOfStatsDict.keys()
    dataForMainStatChart = []

    for stat in primaryStats:
        dataForMainStatChart.append({'stat': stat, 'count': countOfStatsDict[stat]})
    return {'data':dataForMainStatChart}


@user_artifact_routes.route('/<int:user_id>/dataForSetpieceMainStatChart')
def data_for_setpiece_main_stat_chart(user_id):
    user_artifacts = User_Artifact.query\
        .join(User_Artifact.artifact, aliased=True)\
        .filter(User_Artifact.user_id == user_id)\
        .filter(
            or_(
                User_Artifact.artifact.has(slot="Sands of Eon"),
                User_Artifact.artifact.has(slot="Goblet of Eonothem"),
                User_Artifact.artifact.has(slot="Circlet of Logos"))).all()
    countOfStatsDict = {
        'Sands of Eon':{
            'HP%': 0,
            'Elemental Mastery': 0,
            'Energy Recharge': 0,
            'ATK%': 0,
            'DEF%': 0
        },
        'Goblet of Eonothem':{
            'ATK%': 0,
            'DEF%': 0,
            'HP%': 0,
            'Elemental Mastery': 0,
            'PHYS%': 0,
            'ELEM%': 0
        },
        'Circlet of Logos':{
            'ATK%': 0,
            'HP%': 0,
            'DEF%': 0,
            'Elemental Mastery': 0,
            'Healing Bonus': 0,
            'CRIT RATE': 0,
            'CRIT DMG': 0
        }
    }

    for artifact in user_artifacts:
        countOfStatsDict[artifact.artifact.slot][artifact.primary_stat] += 1

    dataForSetpieceMainStatChart = {
        'Sands of Eon': [],
        'Goblet of Eonothem': [],
        'Circlet of Logos': []
    }
    for setpiece in countOfStatsDict:
        # i.e. grab HP, ATK, DEF from Sands... etc
        primaryStatsForSetpiece = countOfStatsDict[setpiece].keys()
        for stat in primaryStatsForSetpiece:
            dataForSetpieceMainStatChart[setpiece].append({'stat': stat, 'count': countOfStatsDict[setpiece][stat]})

    print("DATA MOMENT")
    print(dataForSetpieceMainStatChart)
    return dataForSetpieceMainStatChart
