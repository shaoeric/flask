"""empty message

Revision ID: 76353f08c308
Revises: 
Create Date: 2018-02-23 22:37:43.598769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76353f08c308'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
