from marshmallow import fields, Schema


class MovieSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    trailer = fields.Str(required=True)
    year = fields.Str(required=True)
    rating = fields.Int(required=True)
    genre_id = fields.Int(required=True)
    director_id = fields.Int(required=True)