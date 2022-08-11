from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.profile import Profile

profiles = Blueprint('profiles', 'profiles')

@profiles.route('/', methods=["GET"])
def get_all_profiles():
  profiles = Profile.query.all()
  return jsonify([profile.serialize() for profile in profiles]), 200

@profiles.route('/<id>', methods=["GET"])
def get_one_profile(id):
  profile = Profile.query.filter_by(id=id).first()
  profile_data = profile.serialize()
  return jsonify(profile=profile_data), 200

@profiles.route('/<id>', methods=["GET"])
@login_required
def get_my_profile(id):
  profile = Profile.query.filter_by(id=id).first()
  profile_data = profile.serialize()
  return jsonify(profile=profile_data), 200

@profiles.route('/<id>', methods=["PUT"])
@login_required
def update_profile(id):
  data = request.get_json()
  profile = read_token(request)
  profile = Profile.query.filter_by(id=id)

  for key in data:
    setattr(profile, key, data[key])

  db.session.commit()
  return jsonify(profile.serialize()), 200