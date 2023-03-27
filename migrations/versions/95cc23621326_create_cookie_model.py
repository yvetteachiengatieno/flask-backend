"""create cookie model

Revision ID: 95cc23621326
Revises: 
Create Date: 2023-03-27 20:49:11.649169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95cc23621326'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cookie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=80), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cookie')
    # ### end Alembic commands ###
