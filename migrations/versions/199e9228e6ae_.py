"""empty message

Revision ID: 199e9228e6ae
Revises: 
Create Date: 2025-03-30 17:16:31.824505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '199e9228e6ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('poster', sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###
