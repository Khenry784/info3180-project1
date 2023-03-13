"""empty message

Revision ID: 4d6c13abd3b8
Revises: ea66a8736ea3
Create Date: 2023-03-03 03:02:21.512848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d6c13abd3b8'
down_revision = 'ea66a8736ea3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo', sa.String(length=150), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project1', schema=None) as batch_op:
        batch_op.drop_column('photo')

    # ### end Alembic commands ###
