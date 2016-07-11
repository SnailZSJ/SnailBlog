"""to solve  (OperationalError) no such column: users.confirmed 

Revision ID: 269ff04a071
Revises: None
Create Date: 2016-07-05 12:14:24.989180

"""

# revision identifiers, used by Alembic.
revision = '269ff04a071'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
