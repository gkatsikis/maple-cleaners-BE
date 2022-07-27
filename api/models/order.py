from api.models.db import db 
from datetime import datetime

class Order(db.Model):
  __tablename__ = 'orders'
  id = db.Column(db.Integer, primary_key=True)
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  cost = db.Column(db.Float, default=0.00)
  date = db.Column(db.Date, default=datetime.utcnow, nullable=False)
  comments = db.Column(db.String(250), default='no comment')
  status = db.Column(db.String(10), default='pending')

  def serialize(self):
      order = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return order

