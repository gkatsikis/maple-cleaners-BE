from flask import Blueprint, jsonify, request
from api.middleware import admin_required, read_token

from api.models.db import db
from api.models.profile import Profile

profiles = Blueprint('profiles', 'profiles')

@profiles.route('/profiles', methods=["GET"])
@admin_required
def get_all_profiles():
  profiles = Profile.query.all()
  return jsonify([profile.serialize() for profile in profiles]), 200