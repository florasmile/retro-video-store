"""revised video model

Revision ID: 20c317256407
Revises: da69514ba3ae
Create Date: 2025-05-13 15:03:07.448225

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20c317256407'
down_revision = 'da69514ba3ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('video', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_inventory', sa.Integer(), nullable=False))
        batch_op.alter_column('release_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.drop_column('inventory')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('video', schema=None) as batch_op:
        batch_op.add_column(sa.Column('inventory', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.alter_column('release_date',
               existing_type=sa.String(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
        batch_op.drop_column('total_inventory')

    # ### end Alembic commands ###
