"""Initial migration

Revision ID: 7e28face957a
Revises: 
Create Date: 2024-12-02 23:01:56.360396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e28face957a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plays',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_plays_id'), 'plays', ['id'], unique=False)
    op.create_index(op.f('ix_plays_title'), 'plays', ['title'], unique=False)
    op.create_table('acts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('play_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['play_id'], ['plays.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_acts_id'), 'acts', ['id'], unique=False)
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('play_id', sa.Integer(), nullable=False),
    sa.Column('voice_config', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['play_id'], ['plays.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_characters_id'), 'characters', ['id'], unique=False)
    op.create_table('scenes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('act_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['act_id'], ['acts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_scenes_id'), 'scenes', ['id'], unique=False)
    op.create_table('voice_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('voice_id', sa.String(length=255), nullable=False),
    sa.Column('pitch', sa.Float(), nullable=True),
    sa.Column('speed', sa.Float(), nullable=True),
    sa.Column('settings', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_voice_profiles_id'), 'voice_profiles', ['id'], unique=False)
    op.create_table('dialogues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scene_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('line_number', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['scene_id'], ['scenes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dialogues_id'), 'dialogues', ['id'], unique=False)
    op.create_table('audio_segments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dialogue_id', sa.Integer(), nullable=False),
    sa.Column('file_path', sa.String(length=255), nullable=False),
    sa.Column('duration', sa.Float(), nullable=False),
    sa.Column('start_time', sa.Float(), nullable=False),
    sa.Column('waveform_data', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['dialogue_id'], ['dialogues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_audio_segments_id'), 'audio_segments', ['id'], unique=False)
    op.create_table('stage_directions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('direction_type', sa.Enum('MOVEMENT', 'EMOTION', 'ACTION', 'SETTING', 'LIGHTING', 'SOUND', 'PROP', 'GENERAL', name='directiontype'), nullable=False),
    sa.Column('scene_id', sa.Integer(), nullable=True),
    sa.Column('dialogue_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['dialogue_id'], ['dialogues.id'], ),
    sa.ForeignKeyConstraint(['scene_id'], ['scenes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stage_directions_id'), 'stage_directions', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stage_directions_id'), table_name='stage_directions')
    op.drop_table('stage_directions')
    op.drop_index(op.f('ix_audio_segments_id'), table_name='audio_segments')
    op.drop_table('audio_segments')
    op.drop_index(op.f('ix_dialogues_id'), table_name='dialogues')
    op.drop_table('dialogues')
    op.drop_index(op.f('ix_voice_profiles_id'), table_name='voice_profiles')
    op.drop_table('voice_profiles')
    op.drop_index(op.f('ix_scenes_id'), table_name='scenes')
    op.drop_table('scenes')
    op.drop_index(op.f('ix_characters_id'), table_name='characters')
    op.drop_table('characters')
    op.drop_index(op.f('ix_acts_id'), table_name='acts')
    op.drop_table('acts')
    op.drop_index(op.f('ix_plays_title'), table_name='plays')
    op.drop_index(op.f('ix_plays_id'), table_name='plays')
    op.drop_table('plays')
    # ### end Alembic commands ###
