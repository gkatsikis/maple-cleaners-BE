from flask import Blueprint, jsonify, request
from api.middleware import admin_required, login_required

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