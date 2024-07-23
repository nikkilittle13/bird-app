"""create table birds

Revision ID: 183abf94cf04
Revises: 
Create Date: 2024-07-23 12:33:16.961567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183abf94cf04'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('birds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('birds')
    # ### end Alembic commands ###
