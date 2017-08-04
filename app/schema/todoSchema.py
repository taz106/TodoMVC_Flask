from marshmallow import Schema, fields, validate

class TodoSchema(Schema):
    _id = fields.String(
        required=False
    )
    title = fields.String(
        required=True,
        error_messages={'required': 'Title is required.'} 
    )
    desc = fields.String(
        required=False
    )
    