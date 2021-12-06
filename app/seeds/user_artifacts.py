from app.models import db, User_Artifact

def seed_user_artifacts():
  art1 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 1,
    primary_stat = 'HP',
    primary_stat_value = 457,
    secondary_stat_one = 'CRIT DMG',
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
    secondary_stat_one = 'CRIT RATE',
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
    secondary_stat_one = 'CRIT DMG',
    secondary_stat_one_value = 4.3,
    secondary_stat_two = 'ATK',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'DEF',
    secondary_stat_three_value = 17
  )

  art4 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 3,
    primary_stat = 'ATK',
    primary_stat_value = 117,
    secondary_stat_one = 'CRIT DMG',
    secondary_stat_one_value = 4.3,
    secondary_stat_two = 'ATK',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'DEF',
    secondary_stat_three_value = 17
  )

  art5 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 12,
    primary_stat = 'Elemental Mastery',
    primary_stat_value = 42,
    secondary_stat_one = 'CRIT DMG',
    secondary_stat_one_value = 4.3,
    secondary_stat_two = 'ATK',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'DEF',
    secondary_stat_three_value = 17
  )

  art6 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 7,
    primary_stat = 'Elemental Mastery',
    primary_stat_value = 42,
    secondary_stat_one = 'CRIT DMG',
    secondary_stat_one_value = 4.3,
    secondary_stat_two = 'ATK',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'DEF',
    secondary_stat_three_value = 17
  )

  art7 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 14,
    primary_stat = 'CRIT DMG',
    primary_stat_value = 10.3,
    secondary_stat_one = 'Elemental Mastery',
    secondary_stat_one_value = 4.3,
    secondary_stat_two = 'ATK',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'DEF',
    secondary_stat_three_value = 17
  )

  art8 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 6,
    primary_stat = 'HP',
    primary_stat_value = 457,
    secondary_stat_one = 'CRIT DMG',
    secondary_stat_one_value = 4.3,
    secondary_stat_two = 'ATK',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'DEF',
    secondary_stat_three_value = 17
  )

  art9 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 11,
    primary_stat = 'HP',
    primary_stat_value = 457,
    secondary_stat_one = 'Elemental Mastery',
    secondary_stat_one_value = 4.3,
    secondary_stat_two = 'ATK',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'DEF',
    secondary_stat_three_value = 17
  )

  art10 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 11,
    primary_stat = 'HP',
    primary_stat_value = 457,
    secondary_stat_one = 'Energy Recharge',
    secondary_stat_one_value = 6.7,
    secondary_stat_two = 'DEF',
    secondary_stat_two_value = 10,
    secondary_stat_three = 'DEF%',
    secondary_stat_three_value = 5.3
  )

  art11 = User_Artifact(
    rarity = 5,
    date = '12/5/2021',
    user_id = 1,
    artifact_id = 8,
    primary_stat = 'DEF%',
    primary_stat_value = 117,
    secondary_stat_one = 'Elemental Mastery',
    secondary_stat_one_value = 23,
    secondary_stat_two = 'ATK%',
    secondary_stat_two_value = 5.3,
    secondary_stat_three = 'CRIT RATE',
    secondary_stat_three_value = 6.1
  )

  db.session.add(art1)
  db.session.add(art2)
  db.session.add(art3)
  db.session.add(art4)
  db.session.add(art5)
  db.session.add(art6)
  db.session.add(art7)
  db.session.add(art8)
  db.session.add(art9)
  db.session.add(art10)
  db.session.add(art11)

  db.session.commit()

def undo_user_artifacts():
    db.session.execute('TRUNCATE user_artifacts RESTART IDENTITY CASCADE;')
    db.session.commit()
