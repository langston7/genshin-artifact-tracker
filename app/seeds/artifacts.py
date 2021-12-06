from app.models import db, Artifact

def seed_artifacts():


    witchs_flower_of_blaze = Artifact(
      name='Witch\'s Flower of Blaze',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/0/0f/Item_Witch%27s_Flower_of_Blaze.png',
      set='Crimson Witch of Flames',
      slot='Flower of Life',
    )
    witchs_ever_burning_plume = Artifact(
      name='Witch\'s Ever-Burning Plume',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/b/b3/Item_Witch%27s_Ever-Burning_Plume.png',
      set='Crimson Witch of Flames',
      slot='Plume of Death',
    )
    witchs_end_time = Artifact(
      name='Witch\'s End time',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/1/14/Item_Witch%27s_End_Time.png',
      set='Crimson Witch of Flames',
      slot='Sands of Eon',
    )
    witchs_heart_flames = Artifact(
      name='Witch\'s Heart Flames',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/b/ba/Item_Witch%27s_Heart_Flames.png',
      set='Crimson Witch of Flames',
      slot='Goblet of Eonothem',
    )
    witchs_scorching_hat = Artifact(
      name='Witch\'s Scorching Hat',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/e/ea/Item_Witch%27s_Scorching_Hat.png',
      set='Crimson Witch of Flames',
      slot='Circlet of Logos',
    )


    lavawalkers_resolution = Artifact(
      name='Lavawalker\'s Resolution',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/b/b5/Item_Lavawalker%27s_Resolution.png',
      set='Lavawalker',
      slot='Flower of Life',
    )
    lavawalkers_salvation = Artifact(
      name='Lavawalker\'s Salvation',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/0/0a/Item_Lavawalker%27s_Salvation.png',
      set='Lavawalker',
      slot='Plume of Death',
    )
    lavawalkers_torment = Artifact(
      name='Lavawalker\'s Torment',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/3/3f/Item_Lavawalker%27s_Torment.png',
      set='Lavawalker',
      slot='Sands of Eon',
    )
    lavawalkers_epiphany = Artifact(
      name='Lavawalker\'s Epiphany',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/1/1b/Item_Lavawalker%27s_Epiphany.png',
      set='Lavawalker',
      slot='Goblet of Eonothem',
    )
    lavawalkers_wisdom = Artifact(
      name='Lavawalker\'s Wisdom',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/6/63/Item_Lavawalker%27s_Wisdom.png',
      set='Lavawalker',
      slot='Circlet of Logos',
    )



    royal_flora = Artifact(
      name='Royal Flora',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/7/71/Item_Royal_Flora.png',
      set='Noblesse Oblige',
      slot='Flower of Life',
    )
    royal_plume = Artifact(
      name='Royal Plume',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/e/ee/Item_Royal_Plume.png',
      set='Noblesse Oblige',
      slot='Plume of Death',
    )
    royal_pocket_watch = Artifact(
      name='Royal Pocket Watch',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/1/1a/Item_Royal_Pocket_Watch.png',
      set='Noblesse Oblige',
      slot='Sands of Eon',
    )
    royal_silver_urn = Artifact(
      name='Royal Silver Urn',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/9/9c/Item_Royal_Silver_Urn.png',
      set='Noblesse Oblige',
      slot='Goblet of Eonothem',
    )
    royal_masque = Artifact(
      name='Royal Masque',
      imgsrc='https://static.wikia.nocookie.net/gensin-impact/images/e/eb/Item_Royal_Masque.png',
      set='Noblesse Oblige',
      slot='Circlet of Logos',
    )

    db.session.add(witchs_heart_flames)
    db.session.add(witchs_end_time)
    db.session.add(witchs_ever_burning_plume)
    db.session.add(witchs_flower_of_blaze)
    db.session.add(witchs_scorching_hat)
    db.session.add(lavawalkers_epiphany)
    db.session.add(lavawalkers_resolution)
    db.session.add(lavawalkers_salvation)
    db.session.add(lavawalkers_torment)
    db.session.add(lavawalkers_wisdom)
    db.session.add(royal_flora)
    db.session.add(royal_masque)
    db.session.add(royal_plume)
    db.session.add(royal_pocket_watch)
    db.session.add(royal_silver_urn)


    db.session.commit()


def undo_artifacts():
    db.session.execute('TRUNCATE artifacts RESTART IDENTITY CASCADE;')
    db.session.commit()
