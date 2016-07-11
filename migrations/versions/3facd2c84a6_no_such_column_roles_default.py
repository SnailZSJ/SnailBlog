"""no such column: roles.default

Revision ID: 3facd2c84a6
Revises: 269ff04a071
Create Date: 2016-07-05 22:19:14.586131

"""

# revision identifiers, used by Alembic.
revision = '3facd2c84a6'
down_revision = '269ff04a071'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index('ix_roles_default', 'roles', ['default'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_roles_default', 'roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    ### end Alembic commands ###
