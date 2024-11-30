"""svg

Revision ID: 5ed64c1e5f04
Revises: 288d51ea057d
Create Date: 2024-11-30 16:10:38.792422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ed64c1e5f04'
down_revision = '288d51ea057d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('extra_materials', schema=None) as batch_op:
        batch_op.alter_column('need_to_delete',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('extra_materials', schema=None) as batch_op:
        batch_op.alter_column('need_to_delete',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###
