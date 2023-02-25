"""empty message

Revision ID: f961d3adb6cf
Revises: d99144a8b209
Create Date: 2023-02-20 14:28:50.352861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f961d3adb6cf'
down_revision = 'd99144a8b209'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('florafauna',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('florafauna_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'florafauna', ['florafauna_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('florafauna_id')

    op.drop_table('florafauna')
    # ### end Alembic commands ###
