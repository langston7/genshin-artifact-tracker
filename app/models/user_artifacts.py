from .db import db

class User_Artifact(db.Model):
  __tablename__ = "user_artifacts"

  id = db.Column(db.Integer, primary_key=True)
  rarity = db.Column(db.Integer, nullable=False)
  date = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  artifact_id = db.Column(db.Integer, db.ForeignKey("artifacts.id"))
  primary_stat = db.Column(db.String, nullable=False)
  primary_stat_value = db.Column(db.Integer, nullable=False)
  secondary_stat_one = db.Column(db.String, nullable=False)
  secondary_stat_one_value = db.Column(db.Integer, nullable=False)
  secondary_stat_two = db.Column(db.String, nullable=False)
  secondary_stat_two_value = db.Column(db.Integer, nullable=False)
  secondary_stat_three = db.Column(db.String)
  secondary_stat_three_value = db.Column(db.Integer)
  secondary_stat_four = db.Column(db.String)
  secondary_stat_four_value = db.Column(db.Integer)

  artifact = db.relationship("Artifact")
  user = db.relationship("User", back_populates="artifacts")

  def to_dict(self):
    return {
      'id': self.id,
      'rarity': self.rarity,
      'date': self.date,
      'name': self.artifact.name,
      'image' :self.artifact.imgsrc,
      'artifact_id': self.artifact_id,
      'primary_stat': self.primary_stat,
      'primary_stat_value': self.primary_stat_value,
      'secondary_stat_one': self.secondary_stat_one,
      'secondary_stat_one_value': self.secondary_stat_one_value,
      'secondary_stat_two': self.secondary_stat_two,
      'secondary_stat_two_value': self.secondary_stat_two_value,
      'secondary_stat_three': self.secondary_stat_three,
      'secondary_stat_three_value': self.secondary_stat_three_value,
      'secondary_stat_four': self.secondary_stat_four,
      'secondary_stat_four_value': self.secondary_stat_four_value,
    }
