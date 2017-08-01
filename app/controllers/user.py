from flask import Blueprint
user = Blueprint('user', __name__)

from app.service import *

@user.route('/user')
def get():
    return get_all_user()

@user.route('/user', methods=['POST'])
def post():
    return post_user()

@user.route('/user/<userId>')
def get_user(userId):
    return get_user_By_ID(userId)

@user.route('/user/<userId>', methods=['PATCH'])
def edit_user(userId):
    return patch_user_By_ID(userId)

@user.route('/user/<userId>', methods=["DELETE"])
def delete_user(userId):
    return delete_user_By_ID(userId)