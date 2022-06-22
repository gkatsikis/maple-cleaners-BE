from api.models.db import db 
from datetime import datetime

class Order(db.Model):
  __tablename__ = 'orders'
  id = db.Column(db.Integer, primary_key=True)
  profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  cost = db.Column(db.Float)