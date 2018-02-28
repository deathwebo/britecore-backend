from flask import jsonify
from risker import app
from risker.models import RiskType, EnumOption
from risker.schemas import RiskTypeListSchema, RiskTypeSchema
from sqlalchemy.exc import IntegrityError


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/risk_types", methods=['GET'])
def get_risk_types():
    risk_types = RiskType.query.all()
    risk_types_schema = RiskTypeListSchema(many=True)

    result = risk_types_schema.dump(risk_types)
    return jsonify({'risk_types': result})


@app.route("/risk_types/<int:id>", methods=['GET'])
def get_risk_type(id):
    try:
        risk_type = RiskType.query.get(id)
    except IntegrityError:
        return jsonify({"message": "Risk Type could not be found."}), 400

    risk_type_schema = RiskTypeSchema()
    fields = []
    for field in risk_type.fields:
        field.type = field.field_type.name
        field.options = EnumOption.query.filter_by(field_type_id=field.field_type.id).all()
        fields.append(field)

    risk_type.fields = fields
    result = risk_type_schema.dump(risk_type)
    return jsonify({"risk_type": result})
