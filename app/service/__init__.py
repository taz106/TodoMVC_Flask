from flask import jsonify, request
from bson.objectid import ObjectId
from bson.errors import InvalidId

from app import mongo

from app.schema.userSchema import UserSchema
userSchema = UserSchema()

from app.commonMethods import serialize

def get_all_user():
    res = []
    data = {}
    for user in mongo.db.users.find():
        data, error = userSchema.load(user)
        data['_id'] = str(user['_id'])
        res.append(data)
        print(res) 
    return jsonify({"result": res, "status": 200})

def post_user():
    data = {}
    user,error = userSchema.load(request.json)
    if error:
        return jsonify({"error": error, 'status': 404})
    else:
        res = mongo.db.users.insert(user)
        data = serialize(user)
        return jsonify({'result': data, 'status': 200})

def get_user_By_ID(userId):
    user = {}
    data = {}
    try:
        user = mongo.db.users.find_one({'_id': ObjectId(userId)})
    except InvalidId as err:
        return {"error": str(err), 'status':400}
    if user is None:
        return {"error": "No user found having this {0} id ".format(userId), 'status':404}
    else:
        data = serialize(user)
    return jsonify({'result': data,'status':200})

def patch_user_By_ID(userId):
    user = request.json
    query = {"$set" : user}
    try:
        res = mongo.db.users.update({'_id': ObjectId(userId)}, query)
        if res["n"] == 0:
            return jsonify({"message": "No user to delete having this {0} id ".format(userId), 'status':404})
        else:
            return jsonify({'result': res,'status':200}) 
    except InvalidId as err:
        return {"error": str(err), 'status':400}

def delete_user_By_ID(userId):
    try:
        res = mongo.db.users.remove({'_id': ObjectId(userId)})
        if res["n"] == 0:
            return jsonify({"message": "No user to delete having this {0} id ".format(userId), 'status':404})
        else:
            return jsonify({'result': res,'status':200})
    except InvalidId as err:
        return {"error": str(err), 'status':400}