"""added username

Revision ID: 134f2d0515bd
Revises: a3d7e2f370c0
Create Date: 2023-04-25 13:59:55.406449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '134f2d0515bd'
down_revision = 'a3d7e2f370c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('username')

    # ### end Alembic commands ###
