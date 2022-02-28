"""empty message

Revision ID: ad236cf98869
Revises: df88cbdb48cf
Create Date: 2022-02-24 13:14:45.856956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad236cf98869'
down_revision = 'df88cbdb48cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(), nullable=True))
    op.add_column('user', sa.Column('token_exp', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('is_admin', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'is_admin')
    op.drop_column('user', 'token_exp')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###
