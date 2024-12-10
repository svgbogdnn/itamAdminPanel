"""svg

Revision ID: 4f3ce7cf1811
Revises: 3f50f9afed1d
Create Date: 2024-12-02 23:19:39.561778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f3ce7cf1811'
down_revision = '3f50f9afed1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('extra_materials', schema=None) as batch_op:
        batch_op.alter_column('need_to_delete',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=10),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('extra_materials', schema=None) as batch_op:
        batch_op.alter_column('need_to_delete',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###