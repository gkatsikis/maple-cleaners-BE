from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db 
from api.models.order import Order

orders = Blueprint('orders', 'orders')

@orders.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  order = Order(**data)
  db.session.add(order)
  db.session.commit()
  return jsonify(order.serialize()), 201

@orders.route('/', methods=["GET"])
@login_required
def get_all():
  orders = Order.query.all()
  return jsonify([order.serialize() for order in orders]), 200

@orders.route('/<id>', methods=["GET"])
@login_required
def get_one(id):
  order = Order.query.filter_by(id=id).first()
  order_data = order.serialize()
  return jsonify(order=order_data), 200

@orders.route('/<id>', methods=["PUT"])
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  order = Order.query.filter_by(id=id).first()

  if order.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(order, key, data[key])

  db.session.commit()
  return jsonify(order.serialize()), 200

@orders.route('/<id>', methods=["DELETE"])
@login_required
def delete(id):
  profile = read_token(request)
  order = Order.query.filter_by(id=id).first()

  if order.profile_id != profile["id"]:
    return 'Forbidden', 403

  db.session.delete(order)
  db.session.commit()
  return jsonify(message="Success"), 200