"""Initial migration

Revision ID: 68de793ec2e5
Revises: 
Create Date: 2025-04-02 18:57:56.033961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68de793ec2e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('budget',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('amount_limit', sa.Float(), nullable=False),
    sa.Column('month', sa.String(length=10), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expense',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expense')
    op.drop_table('budget')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###
