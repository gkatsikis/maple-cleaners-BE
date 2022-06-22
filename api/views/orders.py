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