from marshmallow import Schema, fields


class RiskTypeListSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class EnumOptions(Schema):
    value = fields.Str()
    id = fields.Int()


class FieldSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    type = fields.Str()
    options = fields.Nested(EnumOptions, many=True)


class RiskTypeSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    fields = fields.Nested(FieldSchema, many=True)
