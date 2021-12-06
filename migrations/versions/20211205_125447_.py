"""empty message

Revision ID: cb3bc138f5c0
Revises: bc8fc6a84f03
Create Date: 2021-12-05 12:54:47.023948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb3bc138f5c0'
down_revision = 'bc8fc6a84f03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_artifacts', sa.Column('rarity', sa.Integer(), nullable=False))
    op.add_column('user_artifacts', sa.Column('date', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_artifacts', 'date')
    op.drop_column('user_artifacts', 'rarity')
    # ### end Alembic commands ###
