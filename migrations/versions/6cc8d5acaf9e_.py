"""empty message

Revision ID: 6cc8d5acaf9e
Revises: 
Create Date: 2018-02-26 07:33:29.243431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cc8d5acaf9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('field_type',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('date_created', sa.DateTime(), nullable=True),
                    sa.Column('date_updated', sa.DateTime(), nullable=True),
                    sa.Column('name', sa.String(length=256), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('risk_type',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('date_created', sa.DateTime(), nullable=True),
                    sa.Column('date_updated', sa.DateTime(), nullable=True),
                    sa.Column('name', sa.String(length=256), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('enum_option',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('date_created', sa.DateTime(), nullable=True),
                    sa.Column('date_updated', sa.DateTime(), nullable=True),
                    sa.Column('value', sa.String(length=256), nullable=True),
                    sa.Column('field_type_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['field_type_id'], ['field_type.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('field',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('date_created', sa.DateTime(), nullable=True),
                    sa.Column('date_updated', sa.DateTime(), nullable=True),
                    sa.Column('name', sa.String(length=256), nullable=False),
                    sa.Column('risk_type_id', sa.Integer(), nullable=False),
                    sa.Column('field_type_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['field_type_id'], ['field_type.id'], ),
                    sa.ForeignKeyConstraint(['risk_type_id'], ['risk_type.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('field')
    op.drop_table('enum_option')
    op.drop_table('risk_type')
    op.drop_table('field_type')
    # ### end Alembic commands ###
