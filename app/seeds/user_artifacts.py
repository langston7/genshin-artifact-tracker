from app.models import db, User_Artifact

def seed_user_artifacts():
  art1 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 1,
    primary_stat = 'HP',
    primary_stat_value = 2635,
    secondary_stat_one = 'CRIT_DMG',
    secondary_stat_one_value = 4.3,
    secondary_stat_two = 'ATK%',
    secondary_stat_two_value = 5.8,
    secondary_stat_three = 'DEF',
    secondary_stat_three_value = 17
  )

  art2 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 2,
    primary_stat = 'ATK',
    primary_stat_value = 117,
    secondary_stat_one = 'CRIT_RATE',
    secondary_stat_one_value = 2.7,
    secondary_stat_two = 'ATK',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'HP',
    secondary_stat_three_value = 238
  )

  art3 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 3,
    primary_stat = 'Energy Recharge',
    primary_stat_value = 10.3,
    secondary_stat_one = 'CRIT_DMG',
    secondary_stat_one_value = 4.3,
    secondary_stat_two = 'ATK',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'DEF',
    secondary_stat_three_value = 17
  )


  db.session.add(art1)
  db.session.add(art2)
  db.session.add(art3)
  db.session.commit()

def undo_user_artifacts():
    db.session.execute('TRUNCATE user_artifacts RESTART IDENTITY CASCADE;')
    db.session.commit()
