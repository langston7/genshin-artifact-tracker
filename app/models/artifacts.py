from .db import db

class Artifact(db.Model):
  __tablename__ = "artifacts"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  imgsrc = db.Column(db.String, nullable=False)
  set = db.Column(db.String, nullable=False)
  slot = db.Column(db.String, nullable=False)

  user_artifacts = db.relationship("User_Artifact", back_populates="artifact")

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.id,
      'imgsrc': self.imgsrc,
      'set': self.set,
      'slot': self.slot
    }
