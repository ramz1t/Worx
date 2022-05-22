"""first

Revision ID: e8594617198b
Revises: 
Create Date: 2022-05-18 21:54:29.014850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8594617198b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'repos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('owner_username', sa.String)
    )
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String),
        sa.Column('password', sa.String),
        sa.Column('api_key', sa.String)
    )
    op.create_table(
        'AuthSessions',
        sa.Column('token', sa.String, primary_key=True),
        sa.Column('user_id', sa.Integer)
    )


def downgrade():
    op.drop_table('repos')
    op.drop_table('users')
    op.drop_table('AuthSessions')
