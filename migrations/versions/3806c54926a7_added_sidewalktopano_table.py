"""added SidewalkToPano table

Revision ID: 3806c54926a7
Revises: f3b2087436af
Create Date: 2020-03-02 21:23:39.674861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3806c54926a7'
down_revision = 'f3b2087436af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('segment_to_pano',
    sa.Column('linkId', sa.Integer(), nullable=False),
    sa.Column('segmentId', sa.Integer(), nullable=True),
    sa.Column('panoId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['panoId', 'headingDegree'], ['pano.panoId', 'pano.headingDegree'], ),
    sa.ForeignKeyConstraint(['segmentId'], ['sidewalk_segment2.segmentId'], ),
    sa.PrimaryKeyConstraint('linkId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('segment_to_pano')
    # ### end Alembic commands ###
