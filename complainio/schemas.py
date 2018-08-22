from marshmallow import Schema, fields


class CompanySchema(Schema):
    name = fields.Str(required=True)


class LocaleSchema(Schema):
    city = fields.Str(required=True)
    state = fields.Str(required=True)


class ComplainSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    company = fields.Nested(CompanySchema, required=True, many=False)
    locale = fields.Nested(LocaleSchema, required=True, many=False)
