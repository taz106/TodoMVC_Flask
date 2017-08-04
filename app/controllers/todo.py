from flask import Blueprint
todo = Blueprint('todo', __name__)

from app.service import get_all_todo, post_todo, get_todo_By_ID, patch_todo_By_ID, delete_todo_By_ID

@todo.route('/todo')
def get():
    return get_all_todo()

@todo.route('/todo', methods=['POST'])
def post():
    return post_todo()

@todo.route('/todo/<todoID>')
def get_todo(userId):
    return get_todo_By_ID(todoID)

@todo.route('/todo/<todoID>', methods=['PATCH'])
def edit_todo(todoID):
    return patch_todo_By_ID(todoID)

@todo.route('/todo/<todoID>', methods=["DELETE"])
def delete_todo(todoID):
    return delete_todo_By_ID(todoID)