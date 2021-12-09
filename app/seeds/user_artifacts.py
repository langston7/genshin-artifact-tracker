from app.models import db, User_Artifact
import random

FiveStarSubstatArr=[
  {'stat':'HP', 'value':209},
  {'stat':'ATK', 'value':13},
  {'stat':'DEF', 'value':16},
  {'stat':'HP%', 'value':4.1},
  {'stat':'ATK%', 'value':4.1},
  {'stat':'DEF%', 'value':5.1},
  {'stat':'Elemental Mastery', 'value':16},
  {'stat':'Energy Recharge', 'value':4.5},
  {'stat':'CRIT RATE', 'value':2.7},
  {'stat':'CRIT DMG', 'value':5.4}
]

FiveStarSandsMainstatArr=[
  {'stat':'HP%', 'value':7.0},
  {'stat':'ATK%', 'value':7.0},
  {'stat':'DEF%', 'value':8.7},
  {'stat':'Elemental Mastery', 'value':28},
  {'stat':'Energy Recharge', 'value':7.8},
]

FiveStarGobletMainstatArr=[
  {'stat':'HP%', 'value':7.0},
  {'stat':'ATK%', 'value':7.0},
  {'stat':'DEF%', 'value':8.7},
  {'stat':'Elemental Mastery', 'value':28},
  {'stat':'ELEM%', 'value':7.0},
  {'stat':'PHYS%', 'value':8.7},
]

FiveStarCircletMainstatArr=[
  {'stat':'HP%', 'value':7.0},
  {'stat':'ATK%', 'value':7.0},
  {'stat':'DEF%', 'value':8.7},
  {'stat':'Elemental Mastery', 'value':28},
  {'stat':'CRIT RATE', 'value':4.7},
  {'stat':'CRIT DMG', 'value':9.3},
  {'stat':'Healing Bonus', 'value':5.4},
]

def seed_user_artifacts():

  ### FLOWER SEEDS
  for i in range(0, 20):
    # 3 RANDOM SUBSTATS
    randomStats = random.sample(range(10), 3)

    # 5 STEP, ARTIFACTS SHOULD BE SEEDED IN ORDER OF FLOWER-CIRCLET
    randomFlower = random.randrange(1, 12, 5)
    art = User_Artifact(
      rarity = 5,
      date = '12/5/2021',
      user_id = 1,
      artifact_id = randomFlower,
      primary_stat = 'HP',
      primary_stat_value = 717,
      secondary_stat_one = FiveStarSubstatArr[randomStats[0]]['stat'],
      secondary_stat_one_value = FiveStarSubstatArr[randomStats[0]]['value'],
      secondary_stat_two = FiveStarSubstatArr[randomStats[1]]['stat'],
      secondary_stat_two_value = FiveStarSubstatArr[randomStats[1]]['value'],
      secondary_stat_three = FiveStarSubstatArr[randomStats[2]]['stat'],
      secondary_stat_three_value = FiveStarSubstatArr[randomStats[2]]['value'],
    )
    db.session.add(art)


  ### PLUME SEEDS
  for i in range(0, 19):
    randomStats = random.sample(range(10), 3)
    randomPlume = random.randrange(2, 13, 5)
    art = User_Artifact(
      rarity = 5,
      date = '12/5/2021',
      user_id = 1,
      artifact_id = randomPlume,
      primary_stat = 'ATK',
      primary_stat_value = 47,
      secondary_stat_one = FiveStarSubstatArr[randomStats[0]]['stat'],
      secondary_stat_one_value = FiveStarSubstatArr[randomStats[0]]['value'],
      secondary_stat_two = FiveStarSubstatArr[randomStats[1]]['stat'],
      secondary_stat_two_value = FiveStarSubstatArr[randomStats[1]]['value'],
      secondary_stat_three = FiveStarSubstatArr[randomStats[2]]['stat'],
      secondary_stat_three_value = FiveStarSubstatArr[randomStats[2]]['value'],
    )
    db.session.add(art)


  ### SANDS SEEDS
  for i in range(0, 16):
    randomSubstats = random.sample(range(10), 3)
    randomPrimaryStat = random.randrange(5)
    randomSands = random.randrange(3, 14, 5)
    art = User_Artifact(
      rarity = 5,
      date = '12/5/2021',
      user_id = 1,
      artifact_id = randomSands,
      primary_stat = FiveStarSandsMainstatArr[randomPrimaryStat]['stat'],
      primary_stat_value = FiveStarSandsMainstatArr[randomPrimaryStat]['value'],
      secondary_stat_one = FiveStarSubstatArr[randomSubstats[0]]['stat'],
      secondary_stat_one_value = FiveStarSubstatArr[randomSubstats[0]]['value'],
      secondary_stat_two = FiveStarSubstatArr[randomSubstats[1]]['stat'],
      secondary_stat_two_value = FiveStarSubstatArr[randomSubstats[1]]['value'],
      secondary_stat_three = FiveStarSubstatArr[randomSubstats[2]]['stat'],
      secondary_stat_three_value = FiveStarSubstatArr[randomSubstats[2]]['value'],
    )
    db.session.add(art)


  ### GOBLET SEEDS
  for i in range(0, 16):
    randomSubstats = random.sample(range(10), 3)
    randomPrimaryStat = random.randrange(5)
    randomGoblet = random.randrange(4, 15, 5)
    art = User_Artifact(
      rarity = 5,
      date = '12/5/2021',
      user_id = 1,
      artifact_id = randomGoblet,
      primary_stat = FiveStarGobletMainstatArr[randomPrimaryStat]['stat'],
      primary_stat_value = FiveStarGobletMainstatArr[randomPrimaryStat]['value'],
      secondary_stat_one = FiveStarSubstatArr[randomSubstats[0]]['stat'],
      secondary_stat_one_value = FiveStarSubstatArr[randomSubstats[0]]['value'],
      secondary_stat_two = FiveStarSubstatArr[randomSubstats[1]]['stat'],
      secondary_stat_two_value = FiveStarSubstatArr[randomSubstats[1]]['value'],
      secondary_stat_three = FiveStarSubstatArr[randomSubstats[2]]['stat'],
      secondary_stat_three_value = FiveStarSubstatArr[randomSubstats[2]]['value'],
    )
    db.session.add(art)


  ### CIRCLET SEEDS
  for i in range(0, 16):
    randomSubstats = random.sample(range(10), 3)
    randomPrimaryStat = random.randrange(5)
    randomCirclet = random.randrange(5, 16, 5)
    art = User_Artifact(
      rarity = 5,
      date = '12/5/2021',
      user_id = 1,
      artifact_id = randomCirclet,
      primary_stat = FiveStarCircletMainstatArr[randomPrimaryStat]['stat'],
      primary_stat_value = FiveStarCircletMainstatArr[randomPrimaryStat]['value'],
      secondary_stat_one = FiveStarSubstatArr[randomSubstats[0]]['stat'],
      secondary_stat_one_value = FiveStarSubstatArr[randomSubstats[0]]['value'],
      secondary_stat_two = FiveStarSubstatArr[randomSubstats[1]]['stat'],
      secondary_stat_two_value = FiveStarSubstatArr[randomSubstats[1]]['value'],
      secondary_stat_three = FiveStarSubstatArr[randomSubstats[2]]['stat'],
      secondary_stat_three_value = FiveStarSubstatArr[randomSubstats[2]]['value'],
    )
    db.session.add(art)

  db.session.commit()


def undo_user_artifacts():
    db.session.execute('TRUNCATE user_artifacts RESTART IDENTITY CASCADE;')
    db.session.commit()
