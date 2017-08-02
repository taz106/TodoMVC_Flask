from marshmallow import Schema, fields, validate

class TodoSchema(Schema):
    _id = fields.String(
        required=False
    )
    title = fields.String(
        required=True,
        error_messages={'required': 'Name is required.'} 
    )
    description = fields.String(
        required=False
    )
    