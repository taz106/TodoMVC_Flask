def serialize(data):
    obj = {}
    for key,val in data.items():
        if key == '_id':
            obj['_id'] = str(data['_id'])
        else:
            obj[key] = val
    return obj