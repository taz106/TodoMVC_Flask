from flask import jsonify, request
from bson.objectid import ObjectId
from bson.errors import InvalidId

from app import mongo

from app.schema.todoSchema import TodoSchema
todoSchema = TodoSchema()

from app.commonMethods import serialize

def get_all_todo():
    res = []
    data = {}
    for todo in mongo.db.todos.find():
        data, error = todoSchema.load(todo)
        data['_id'] = str(todo['_id'])
        res.append(data)
        print(res) 
    return jsonify({"result": res, "status": 200})

def post_todo():
    data = {}
    todo,error = todoSchema.load(request.json)
    if error:
        return jsonify({"error": error, 'status': 404})
    else:
        res = mongo.db.todos.insert(user)
        data = serialize(user)
        return jsonify({'result': data, 'status': 200})

def get_todo_By_ID(todoID):
    todo = {}
    data = {}
    try:
        todo = mongo.db.todos.find_one({'_id': ObjectId(todoID)})
    except InvalidId as err:
        return {"error": str(err), 'status':400}
    if todo is None:
        return {"error": "No Task found having this {0} id ".format(todoID), 'status':404}
    else:
        data = serialize(todo)
    return jsonify({'result': data,'status':200})

def patch_todo_By_ID(todoID):
    todo = request.json
    query = {"$set" : todo}
    try:
        res = mongo.db.todos.update({'_id': ObjectId(todoID)}, query)
        if res["n"] == 0:
            return jsonify({"message": "No Task to delete having this {0} id ".format(todoID), 'status':404})
        else:
            return jsonify({'result': res,'status':200}) 
    except InvalidId as err:
        return {"error": str(err), 'status':400}

def delete_todo_By_ID(todoID):
    try:
        res = mongo.db.todos.remove({'_id': ObjectId(todoID)})
        if res["n"] == 0:
            return jsonify({"message": "No user to delete having this {0} id ".format(todoID), 'status':404})
        else:
            return jsonify({'result': res,'status':200})
    except InvalidId as err:
        return {"error": str(err), 'status':400}