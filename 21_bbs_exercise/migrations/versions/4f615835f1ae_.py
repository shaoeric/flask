"""empty message

Revision ID: 4f615835f1ae
Revises: 
Create Date: 2018-03-01 17:08:27.424139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f615835f1ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cms_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('join_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cms_user')
    # ### end Alembic commands ###