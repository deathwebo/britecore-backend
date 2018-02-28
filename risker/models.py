from risker import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime, default=db.func.current_timestamp(),
                             onupdate=db.func.current_timestamp())


class RiskType(Base):
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)


class Field(Base):
    name = db.Column(db.String(256), nullable=False)
    risk_type_id = db.Column(db.Integer, db.ForeignKey('risk_type.id'),
                             nullable=False)
    risk_type = db.relationship('RiskType',
                                backref=db.backref('fields', lazy=True))
    field_type_id = db.Column(db.Integer, db.ForeignKey('field_type.id'),
                              nullable=False)


class FieldType(Base):
    name = db.Column(db.String(256), nullable=False)
    field = db.relationship('Field', backref=db.backref('field_type', lazy=True))


class EnumOption(Base):
    value = db.Column(db.String(256))
    field_type_id = db.Column(db.Integer, db.ForeignKey('field_type.id'),
                              nullable=False)
    field_type = db.relationship('FieldType',
                                 backref=db.backref('enum_options', lazy=True))
