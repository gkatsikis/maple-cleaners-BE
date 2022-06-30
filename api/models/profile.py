from datetime import datetime
from api.models.db import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100))
    zipcode = db.Column(db.Integer) # how can I allow first zero?
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    balance = db.Column(db.Float, default=0.00)
    role = db.Column(db.String(100), default='customer')
    
    orders = db.relationship('Order', backref='profile', lazy=True)

    def serialize(self):
      profile = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return profile