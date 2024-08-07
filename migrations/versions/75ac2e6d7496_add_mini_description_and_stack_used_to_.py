"""Add mini_description and stack_used to Project

Revision ID: 75ac2e6d7496
Revises: 
Create Date: 2024-08-06 16:40:31.805311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75ac2e6d7496'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mini_description', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('stack_used', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('stack_used')
        batch_op.drop_column('mini_description')

    # ### end Alembic commands ###