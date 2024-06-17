"""operation refactor

Revision ID: 950f63e483c3
Revises: 80cecb929c01
Create Date: 2024-06-15 19:22:29.098972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '950f63e483c3'
down_revision: Union[str, None] = '80cecb929c01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('investment_profile_strategy_investment_profile_id_fkey', 'investment_profile_strategy', type_='foreignkey')
    op.drop_constraint('investment_profile_strategy_strategy_id_fkey', 'investment_profile_strategy', type_='foreignkey')
    
    # Agrega la enumeración 'operation_type'
    operation_type_enum = sa.Enum('buy', 'sell', name='operation_type')
    operation_type_enum.create(op.get_bind())
    
    # Agrega la columna 'operation_type' a la tabla 'operation'
    op.add_column('operation', sa.Column('operation_type', operation_type_enum, nullable=False))
    
    # Continúa con las demás operaciones
    op.add_column('operation', sa.Column('asset', sa.String(length=100), nullable=False))
    op.add_column('operation', sa.Column('operation_date', sa.DateTime(), nullable=False))
    op.add_column('operation', sa.Column('amount', sa.Numeric(precision=15, scale=2), nullable=False))
    op.add_column('operation', sa.Column('unit_price', sa.Numeric(precision=15, scale=2), nullable=False))
    op.add_column('operation', sa.Column('total_return', sa.Numeric(precision=15, scale=2), nullable=False))
    op.add_column('operation', sa.Column('investment_profile_id', sa.Integer(), nullable=False))
    op.add_column('operation', sa.Column('strategy_id', sa.Integer(), nullable=False))
    
    # Elimina las dependencias de la columna 'period'
    op.drop_constraint('operation_id_strategy_fkey', 'operation', type_='foreignkey')
    op.drop_constraint('operation_id_profile_fkey', 'operation', type_='foreignkey')
    
    # Elimina la columna 'period'
    op.drop_column('operation', 'period')
    
    # Crea el tipo ENUM 'period' explícitamente
    period_enum = sa.Enum('Period 1', 'Period 2', 'Period 3', name='period')
    period_enum.create(op.get_bind())
    
    # Agrega la nueva columna 'period' con el tipo enumerado
    op.add_column('operation', sa.Column('period', period_enum, nullable=False))
    
    op.create_foreign_key('fk_operation_investment_profile_strategy', 'operation', 'investment_profile_strategy', ['investment_profile_id', 'strategy_id'], ['investment_profile_id', 'strategy_id'])
    op.drop_column('operation', 'end_date')
    op.drop_column('operation', 'start_date')
    op.drop_column('operation', 'total')
    op.drop_column('operation', 'id_profile')
    op.drop_column('operation', 'price')
    op.drop_column('operation', 'id_strategy')


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operation', sa.Column('id_strategy', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('operation', sa.Column('price', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('operation', sa.Column('id_profile', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('operation', sa.Column('total', sa.NUMERIC(), autoincrement=False, nullable=True))
    op.add_column('operation', sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=True))
    op.add_column('operation', sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_constraint('fk_operation_investment_profile_strategy', 'operation', type_='foreignkey')
    op.create_foreign_key('operation_id_profile_fkey', 'operation', 'investment_profile', ['id_profile'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('operation_id_strategy_fkey', 'operation', 'strategy', ['id_strategy'], ['id'], ondelete='CASCADE')
    op.alter_column('operation', 'period',
               existing_type=sa.Enum('Period 1', 'Period 2', 'Period 3', name='period'),
               type_=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_column('operation', 'strategy_id')
    op.drop_column('operation', 'investment_profile_id')
    op.drop_column('operation', 'total_return')
    op.drop_column('operation', 'unit_price')
    op.drop_column('operation', 'amount')
    op.drop_column('operation', 'operation_type')
    op.drop_column('operation', 'operation_date')
    op.drop_column('operation', 'asset')
    op.create_foreign_key('investment_profile_strategy_strategy_id_fkey', 'investment_profile_strategy', 'strategy', ['strategy_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('investment_profile_strategy_investment_profile_id_fkey', 'investment_profile_strategy', 'investment_profile', ['investment_profile_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###