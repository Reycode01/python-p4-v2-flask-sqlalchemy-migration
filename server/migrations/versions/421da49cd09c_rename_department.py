"""rename department

Revision ID: 421da49cd09c
Revises: 836b7806f8cf
Create Date: 2024-07-01 14:04:04.461627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '421da49cd09c'
down_revision = '836b7806f8cf'
branch_labels = None
depends_on = None


def upgrade():
    # Rename the column 'address' to 'location' in 'departments' table
    op.alter_column('departments', 'address', new_column_name='location')


def downgrade():
    # Rename the column 'location' back to 'address' in 'departments' table
    op.alter_column('departments', 'location', new_column_name='address')

