"""New field description in investment profile table

Revision ID: c83be8ff7050
Revises: f0e36e9d8a02
Create Date: 2024-04-01 23:22:38.314089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c83be8ff7050'
down_revision: Union[str, None] = 'f0e36e9d8a02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('investment_profile', sa.Column('description', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('investment_profile', 'description')
    # ### end Alembic commands ###
