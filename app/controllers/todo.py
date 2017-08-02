from flask import Blueprint
todo = Blueprint('todo', __name__)

from app.service import get_all_todo, post_todo, get_todo_By_ID, patch_todo_By_ID, delete_todo_By_ID

@user.route('/todo')
def get():
    return get_all_todo()

@user.route('/todo', methods=['POST'])
def post():
    return post_todo()

@user.route('/todo/<todoID>')
def get_todo(userId):
    return get_todo_By_ID(todoID)

@user.route('/todo/<todoID>', methods=['PATCH'])
def edit_todo(userId):
    return patch_todo_By_ID(todoID)

@user.route('/todo/<todoID>', methods=["DELETE"])
def delete_todo(userId):
    return delete_todo_By_ID(todoID)