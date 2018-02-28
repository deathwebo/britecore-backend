import click
from risker import app
from risker import db
from risker.models import RiskType, Field, FieldType, EnumOption
from flask_migrate import upgrade


@app.cli.command()
def populatedb():
    """Populate the database with test data."""
    click.echo('Initializing db')

    field_type_text = FieldType(name="text")
    field_type_number = FieldType(name="number")
    field_type_date = FieldType(name="date")
    field_type_enum = FieldType(name="enum")
    db.session.add_all([field_type_text, field_type_number,
                        field_type_date, field_type_enum])

    enum_option1 = EnumOption(value="low")
    enum_option2 = EnumOption(value="medium")
    enum_option3 = EnumOption(value="high")
    db.session.add_all([enum_option1, enum_option2, enum_option3])

    field_type_enum.enum_options.append(enum_option1)
    field_type_enum.enum_options.append(enum_option2)
    field_type_enum.enum_options.append(enum_option3)

    risk_automobiles = RiskType(name="automobiles", description="Risk of type automobiles")
    db.session.add(risk_automobiles)

    field_car_maker = Field(name="Car Maker")
    field_car_maker.field_type = field_type_text

    field_car_model = Field(name="Car Model")
    field_car_model.field_type = field_type_text

    field_car_year = Field(name="Year")
    field_car_year.field_type = field_type_number

    db.session.add_all([field_car_maker, field_car_model, field_car_year])

    risk_automobiles.fields = [field_car_maker, field_car_model, field_car_year]

    risk_houses = RiskType(name="houses", description="Risk of type houses")
    db.session.add(risk_houses)

    field_address = Field(name="address")
    field_address.field_type = field_type_text

    field_area = Field(name="area")
    field_area.field_type = field_type_number

    db.session.add_all([field_address, field_area])

    risk_houses.fields = [field_address, field_area]

    risk_prizes = RiskType(name="prizes", description="Risk of type prizes")
    db.session.add(risk_prizes)

    field_impact = Field(name="Impact")
    field_impact.field_type = field_type_enum

    field_expiration_date = Field(name="Expiration Date")
    field_expiration_date.field_type = field_type_date

    db.session.add_all([field_impact, field_expiration_date])

    risk_prizes.fields = [field_impact, field_expiration_date]

    db.session.commit()


@app.cli.command()
def createdb():
    """Initialize the database to the latest migration version."""
    upgrade()
    click.echo("Database structure created")
