"""empty message

Revision ID: 8ed9599d1b2c
Revises: 
Create Date: 2019-07-26 00:13:49.689658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ed9599d1b2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voice_of_seren',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('current_voice_one', sa.String(), nullable=True),
    sa.Column('current_voice_two', sa.String(), nullable=True),
    sa.Column('message_id', sa.String(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voice_of_seren')
    # ### end Alembic commands ###
