"""empty message

Revision ID: cefb50c219c5
Revises: b02cedca3b67
Create Date: 2019-04-06 13:44:13.790014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cefb50c219c5'
down_revision = 'b02cedca3b67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('raidsstate', sa.Column('time_to_next_message', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('raidsstate', 'time_to_next_message')
    # ### end Alembic commands ###
