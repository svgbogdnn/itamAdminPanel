"""Added institute column to users

Revision ID: 72f9ee960f4b
Revises: 28ba702cae78
Create Date: 2024-11-29 16:10:33.519050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72f9ee960f4b'
down_revision = '28ba702cae78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('institute', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('institute')

    # ### end Alembic commands ###
