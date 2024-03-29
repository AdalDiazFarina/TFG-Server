"""Naming duracion field to duration

Revision ID: f0e36e9d8a02
Revises: 7fd15ece5ed9
Create Date: 2024-03-21 15:49:15.975746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0e36e9d8a02'
down_revision: Union[str, None] = '7fd15ece5ed9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('investment_profile', sa.Column('duration', sa.Date(), nullable=True))
    op.drop_column('investment_profile', 'duracion')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('investment_profile', sa.Column('duracion', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('investment_profile', 'duration')
    # ### end Alembic commands ###
