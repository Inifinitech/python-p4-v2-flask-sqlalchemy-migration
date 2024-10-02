"""rename department

Revision ID: d612b8c29866
Revises: ebe78ca83d7f
Create Date: 2024-10-02 17:21:28.089664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd612b8c29866'
down_revision = 'ebe78ca83d7f'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
