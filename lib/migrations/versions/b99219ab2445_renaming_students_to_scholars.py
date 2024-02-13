"""Renaming students to scholars

Revision ID: b99219ab2445
Revises: 791279dd0760
Create Date: 2024-02-13 12:44:03.354368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b99219ab2445'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
