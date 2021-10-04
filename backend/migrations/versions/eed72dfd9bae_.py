"""empty message

Revision ID: eed72dfd9bae
Revises: 
Create Date: 2021-08-24 16:32:32.582795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eed72dfd9bae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('client_api', sa.String(length=128), nullable=False),
    sa.Column('ticker_time', sa.String(length=256), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('ticker', sa.String(length=10), nullable=False),
    sa.Column('buy_price', sa.Float(), nullable=True),
    sa.Column('buy_time', sa.DateTime(), nullable=True),
    sa.Column('quantity', sa.Float(), nullable=True),
    sa.Column('fee', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ticker_time')
    )
    op.create_table('coin',
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('ticker_date', sa.String(length=20), nullable=False),
    sa.Column('ticker', sa.String(length=10), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('open', sa.Float(), nullable=True),
    sa.Column('high', sa.Float(), nullable=True),
    sa.Column('low', sa.Float(), nullable=True),
    sa.Column('close', sa.Float(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ticker_date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coin')
    op.drop_table('client')
    # ### end Alembic commands ###
