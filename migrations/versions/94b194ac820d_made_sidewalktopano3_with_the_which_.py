"""made sidewalkToPano3 with the which endpoint indicator

Revision ID: 94b194ac820d
Revises: bd0b4477ae02
Create Date: 2020-03-22 10:17:48.803094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94b194ac820d'
down_revision = 'bd0b4477ae02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('segment_to_pano3',
    sa.Column('linkId', sa.Integer(), nullable=False),
    sa.Column('segmentId', sa.Integer(), nullable=True),
    sa.Column('whichEndpoint', sa.Text(), nullable=True),
    sa.Column('panoId', sa.Integer(), nullable=True),
    sa.Column('headingDegree', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['segmentId'], ['sidewalk_segment3.segmentId'], ),
    sa.PrimaryKeyConstraint('linkId')
    )
    op.add_column('pano_feature', sa.Column('updateTs', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pano_feature', 'updateTs')
    op.drop_table('segment_to_pano3')
    # ### end Alembic commands ###
