"""date field added in Expense table

Revision ID: d0290917e6b8
Revises: 6433fdf826ad
Create Date: 2024-12-30 13:30:08.864529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0290917e6b8'
down_revision = '6433fdf826ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Expense', schema=None) as batch_op:
        batch_op.add_column(sa.Column('expense_date', sa.Date(), nullable=False, server_default=sa.text("'1998-01-01'")))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Expense', schema=None) as batch_op:
        batch_op.drop_column('expense_date')

    # ### end Alembic commands ###