"""add incident field values

Revision ID: 25a10d717000
Revises: d76e19f6e3b6
Create Date: 2024-07-15 19:16:07.638828

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "25a10d717000"
down_revision: Union[str, None] = "d76e19f6e3b6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "incident_field_value",
        sa.Column("id", sa.String(length=50), nullable=False),
        sa.Column("incident_id", sa.String(length=50), nullable=False),
        sa.Column("field_id", sa.String(length=50), nullable=False),
        sa.Column("value_text", sa.String(), nullable=True),
        sa.Column("value_textarea", sa.String(), nullable=True),
        sa.Column("value_single_select", sa.String(), nullable=True),
        sa.Column("value_multi_select", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["field_id"], ["field.id"], ondelete="cascade"),
        sa.ForeignKeyConstraint(["incident_id"], ["incident.id"], ondelete="cascade"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_incident_field_value_field_id"), "incident_field_value", ["field_id"], unique=False)
    op.create_index(op.f("ix_incident_field_value_incident_id"), "incident_field_value", ["incident_id"], unique=False)
    op.drop_index("ix_custom_field_organisation_id", table_name="field")
    op.create_index(op.f("ix_field_organisation_id"), "field", ["organisation_id"], unique=False)
    op.drop_index("ix_form_field_custom_field_id", table_name="form_field")
    op.create_index(op.f("ix_form_field_field_id"), "form_field", ["field_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_form_field_field_id"), table_name="form_field")
    op.create_index("ix_form_field_custom_field_id", "form_field", ["field_id"], unique=False)
    op.drop_index(op.f("ix_field_organisation_id"), table_name="field")
    op.create_index("ix_custom_field_organisation_id", "field", ["organisation_id"], unique=False)
    op.drop_index(op.f("ix_incident_field_value_incident_id"), table_name="incident_field_value")
    op.drop_index(op.f("ix_incident_field_value_field_id"), table_name="incident_field_value")
    op.drop_table("incident_field_value")
    # ### end Alembic commands ###
