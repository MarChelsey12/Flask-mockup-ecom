"""empty message

Revision ID: 675230ab355f
Revises: bc595f6786e9
Create Date: 2022-02-27 20:14:52.352373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '675230ab355f'
down_revision = 'bc595f6786e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shopping_cart',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('item_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopping_cart')
    # ### end Alembic commands ###
