"""empty message

Revision ID: 66aee9f0168d
Revises: 
Create Date: 2022-04-15 02:31:23.856647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66aee9f0168d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('no', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###