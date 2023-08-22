"""changes table name to users

Revision ID: a7cebe4f3a4d
Revises: fea918a10e81
Create Date: 2023-08-21 22:17:21.220362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7cebe4f3a4d'
down_revision: Union[str, None] = 'fea918a10e81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('user', 'users')


def downgrade() -> None:
    op.rename_table('users', 'user')
